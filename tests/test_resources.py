"""Behavioral checks for bundled and private, read-only resource lookup."""
import hashlib
import json
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def run(root, *args):
    process = subprocess.run([sys.executable, str(root / "scripts/search_resources.py"), *args],
                             capture_output=True, text=True, encoding="utf-8")
    return process.returncode, json.loads(process.stdout)


class ResourceTests(unittest.TestCase):
    def test_documentation_links_resolve_inside_skill(self):
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "private", "__pycache__"} for part in path.relative_to(ROOT).parts):
                continue
            for href in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if href.startswith(("https:", "http:", "#")):
                    continue
                target = (path.parent / href.split("#")[0]).resolve()
                self.assertTrue(target.is_relative_to(ROOT.resolve()), (path, href))
                self.assertTrue(target.is_file(), (path, href))

    def test_manifest_points_to_real_content(self):
        manifest = json.loads((ROOT / "resources/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["mode"], "author-specific")
        for entry in manifest["resources"]:
            path = ROOT / entry["path"]
            self.assertTrue(path.is_file(), entry)
            self.assertGreater(len(path.read_text(encoding="utf-8")), 100)

    def test_bundled_search_returns_context_not_empty_profile(self):
        code, data = run(ROOT, "退阶练习", "--scope", "bundled", "--limit", "4")
        self.assertEqual(code, 0)
        self.assertFalse(data["private_config_used"])
        self.assertTrue(any("CTX-S44" in hit["heading"] for hit in data["results"]))
        for hit in data["results"]:
            self.assertEqual(hit["kind"], "bundled")
            self.assertTrue((ROOT / hit["path"]).is_file())
            self.assertGreaterEqual(hit["line_start"], 1)
            self.assertGreaterEqual(hit["line_end"], hit["line_start"])

    def test_interests_and_careers_are_available(self):
        code, data = run(ROOT, "兴趣 职业", "--scope", "bundled", "--limit", "8")
        self.assertEqual(code, 0)
        self.assertTrue(any("CTX-S09" in h["heading"] or "W04" in h["heading"] for h in data["results"]))

    def isolated_copy(self, destination):
        shutil.copytree(ROOT / "scripts", destination / "scripts")
        shutil.copytree(ROOT / "resources", destination / "resources")

    def test_auto_works_without_private_sources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.isolated_copy(root)
            code, data = run(root, "机会", "--limit", "2")
            self.assertEqual(code, 0)
            self.assertFalse(data["private_config_used"])
            self.assertTrue(data["results"])

    def test_local_lookup_reads_registered_source_without_mutation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.isolated_copy(root)
            private = root / "private"
            private.mkdir()
            source = private / "fixture.md"
            source.write_text("# Local context\n\n独特测试卡点：退阶不是取消原目标。\n", encoding="utf-8")
            before = hashlib.sha256(source.read_bytes()).hexdigest()
            (private / "sources.json").write_text(json.dumps({"sources": [
                {"id": "test-chat", "kind": "original_chat", "path": str(source)}
            ]}), encoding="utf-8")
            code, data = run(root, "独特测试卡点", "--scope", "local")
            self.assertEqual(code, 0)
            self.assertTrue(data["private_config_used"])
            self.assertEqual(data["results"][0]["source_id"], "test-chat")
            self.assertEqual(data["results"][0]["kind"], "original_chat")
            self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), before)

    def test_explicit_local_mode_reports_missing_connection(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.isolated_copy(root)
            code, data = run(root, "兴趣", "--scope", "local")
            self.assertEqual(code, 2)
            self.assertFalse(data["results"])
            self.assertTrue(data["warnings"])


if __name__ == "__main__":
    unittest.main()
