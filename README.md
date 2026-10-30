# Windowsill Essay Studio

**Personal viewpoints. Thoughtful long-form essays. Original visuals. Platform-aware delivery.**

A Chinese-language writing skill for Codex and compatible coding agents. It turns source conversations, an author's existing work and authorized book notes into complete viewpoint essays—not stitched quotations, generic outlines or invented personal stories.

The repository name and interface title are English; the core writing instructions are primarily Chinese because the workflow targets Chinese essays and publishing platforms.

## What it does

- **Understand before extending.** Read the full exchange, distinguish speakers, preserve conditions and separate source material from editorial inference.
- **Write a real essay.** Start from a concrete event or decision, develop a defensible viewpoint, address counterarguments and deliver a useful conclusion. Roughly 3,000–5,000 Chinese characters is a starting preference, not a quota.
- **Build an author's voice.** Borrow useful narrative techniques without adopting another creator's identity, catchphrases or experiences.
- **Use a reading library responsibly.** When the author explicitly authorizes it, integrate book ideas as internalized values while preserving attribution and the distinction between ideas and lived experience.
- **Create consistent visuals.** Plan original illustrations and use HTML rendering for text-heavy cards and cover typography. Actual illustration generation requires an available image backend.
- **Adapt to each platform.** Inline HTML for WeChat, native formatting for Zhihu, and local text/image packages for Xiaohongshu.
- **Verify delivery.** Distinguish local files, remote drafts, public posts and mass sends. Publishing requires an explicit request and working authorized tools.

## Install

Clone this repository into a skill directory named `windowsill-essay-studio` under your Codex skills root. Use `$CODEX_HOME/skills` when configured, otherwise `~/.codex/skills`.

```bash
git clone https://github.com/ljyhavefun-ai/windowsill-essay-studio.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/windowsill-essay-studio"
```

PowerShell:

```powershell
$root = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path $HOME '.codex/skills'
}
New-Item -ItemType Directory -Force -Path $root | Out-Null
git clone https://github.com/ljyhavefun-ai/windowsill-essay-studio.git `
    (Join-Path $root 'windowsill-essay-studio')
```

If that destination already exists, inspect it before updating; do not overwrite a personalized installation blindly. Refresh or start a new agent session if the skill does not appear yet. Other agents can load `SKILL.md` explicitly using their supported mechanism.

## Use

```text
使用 $windowsill-essay-studio，结合我提供的完整对话和读书笔记，
写一篇关于“好建议为什么未必适合我”的长文章。只写稿，不推送。
```

```text
使用 $windowsill-essay-studio，只排版这份定稿，文字和标点不改。
输出公众号HTML及知乎版本，不上传平台。
```

```text
使用 $windowsill-essay-studio，为定稿制作原创插图与封面，
并推送公众号草稿箱。小红书只交付无空行TXT和本地图片。
```

Provide your sources and voice preferences in a **private workspace**, not in this repository. See [workspace setup](references/local-environment.md). A new user's books are not automatically treated as their beliefs; that is an explicit author preference.

## Components

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Entry point, routing and essential boundaries |
| [source-context.md](references/source-context.md) | Source provenance, speaker attribution and book integration |
| [writing.md](references/writing.md) | Topic selection, long-form argument and voice editing |
| [visuals-platforms.md](references/visuals-platforms.md) | Original visual language and platform formatting |
| [publishing.md](references/publishing.md) | Authorization, retries, persistence checks and delivery states |
| [local-environment.md](references/local-environment.md) | Portable workspace setup and optional dependencies |

Specialized skills are **optional integrations, not bundled implementations**. Read their current instructions when actually using them. Missing credentials or browser access cannot be solved by installing this writing workflow alone. No universal “one-click publishing” or traffic guarantee is claimed.

## Defaults you should know

- WeChat “push” means **save to the draft box**, not public release or mass send.
- Zhihu delivery uses the requested article/answer and draft/public scope; verify it after saving.
- Xiaohongshu is **manual delivery only**: local images and UTF-8 text without blank lines. No automatic login, upload, draft saving or posting.
- Typesetting preserves the finalized wording. Rewriting and content adaptation are separate operations.
- No invented experiences, deliberate typos or promises to evade AI detectors. Follow mandatory platform disclosures honestly.
- Source chats, book libraries, local paths, credentials and delivery receipts are not included in the public package.

## Credits and license

The integration, editorial decisions and workflow instructions in this repository are released under the [MIT License](LICENSE). See [third-party acknowledgments](THIRD_PARTY.md) for referenced skills. Their implementations and assets are not included and retain their respective licenses. No affiliation or endorsement is implied.
