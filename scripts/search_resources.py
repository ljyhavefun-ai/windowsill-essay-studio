#!/usr/bin/env python3
"""Read-only search of bundled author resources and explicitly registered local sources."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sections(path: Path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = 0
    if lines and lines[0] == "---":
        for i in range(1, len(lines)):
            if lines[i] == "---":
                start = i + 1
                break
    points = [i for i in range(start, len(lines)) if re.match(r"^#{1,6}\s+", lines[i])]
    if start < len(lines) and (not points or points[0] > start):
        points.insert(0, start)
    for n, begin in enumerate(points):
        end = points[n + 1] if n + 1 < len(points) else len(lines)
        text = "\n".join(lines[begin:end]).strip()
        if text:
            yield begin + 1, end, lines[begin].lstrip("# "), text


def discover(scope: str):
    entries = [(p, "bundled", "author-bundle") for p in sorted((ROOT / "resources").rglob("*.md"))]
    warnings = []
    config = ROOT / "private" / "sources.json"
    if scope == "bundled":
        return entries, warnings, False
    if not config.exists():
        if scope == "local":
            warnings.append("No private/sources.json is available; no local sources were read.")
        return entries if scope == "auto" else [], warnings, False
    if scope == "local":
        entries = []
    data = json.loads(config.read_text(encoding="utf-8-sig"))
    for item in data.get("sources", []):
        origin = Path(item["path"]).expanduser().resolve()
        if not origin.exists():
            warnings.append("Missing registered source: " + item["id"])
            continue
        if origin.is_file():
            candidates = [origin]
        else:
            iterator = origin.rglob("*") if item.get("recursive", False) else origin.glob("*")
            candidates = sorted(p for p in iterator if p.is_file() and p.suffix.lower() in {".md", ".txt"})
        for p in candidates:
            resolved = p.resolve()
            if origin.is_dir() and not resolved.is_relative_to(origin):
                warnings.append("Skipped path outside registered directory: " + item["id"])
                continue
            if resolved.suffix.lower() not in {".md", ".txt"}:
                warnings.append("Unsupported source format: " + item["id"])
                continue
            entries.append((resolved, item.get("kind", "local"), item["id"]))
    seen = set()
    unique = []
    for item in entries:
        key = str(item[0].resolve()).casefold()
        if key not in seen:
            unique.append(item)
            seen.add(key)
    return unique, warnings, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--scope", choices=["auto", "bundled", "local"], default="auto")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--stats", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        parser.error("--limit must be between 1 and 20")
    if not args.query.strip() and not args.stats:
        parser.error("provide a query, or use --stats")
    entries, warnings, private = discover(args.scope)
    terms = list(dict.fromkeys(re.findall(r"[^\s,，;；]+", args.query.casefold())))
    hits = []
    section_count = 0
    for path, kind, source_id in entries:
        try:
            chunks = list(sections(path))
        except (OSError, UnicodeError) as exc:
            warnings.append("Cannot read " + source_id + ": " + type(exc).__name__)
            continue
        section_count += len(chunks)
        for start, end, heading, text in chunks:
            normalized = text.casefold()
            matched = [term for term in terms if term in normalized]
            if not matched:
                continue
            score = sum(6 + min(normalized.count(t), 5) + (8 if t in heading.casefold() else 0) for t in matched)
            first = min(normalized.index(t) for t in matched)
            clip_start = max(0, first - 160) if len(text) > 900 else 0
            excerpt = text[clip_start:clip_start + 900]
            shown_path = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
            hits.append({"score": score, "kind": kind, "source_id": source_id, "path": shown_path,
                         "heading": heading, "line_start": start, "line_end": end,
                         "matched_terms": matched, "excerpt": excerpt,
                         "full_section": clip_start == 0 and len(excerpt) == len(text)})
    hits.sort(key=lambda x: (-x["score"], x["path"], x["line_start"]))
    result = {"query": args.query, "scope": args.scope, "private_config_used": private,
              "documents": len(entries), "sections": section_count, "matches": len(hits),
              "results": hits[:args.limit], "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if args.scope == "local" and not private else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({"error": type(exc).__name__, "detail": "Check registered local-source configuration."}))
        raise SystemExit(2)
