# Workspace Setup and Optional Dependencies

This public package contains a writing workflow, not the original author's private workspace, books, credentials, or chat history. Configure your own sources; never infer access or authorization from an example path.

## Private workspace configuration

Choose a workspace and keep the following locally, outside this repository:

| Configuration | What it identifies |
|---|---|
| `WORKSPACE` | Article drafts, topic history, internal source records and platform variants |
| `BOOKS_ROOT` | The Obsidian book notes or other reading material the author permits you to use |
| `AUTHOR_PROFILE` | Voice samples, preferences, current values, signature choice and book-internalization consent |
| `SOURCE_INDEX` | Source files, conversation regions and speaker-confidence notes |

These are configuration concepts, not required environment variables. Resolve them from the current request or an explicitly supplied private profile. Do not invent paths, scan unrelated disks, or claim to have read unavailable sources. Keep originals read-only unless the user requests an edit.

The original author's specific views, reading history and publication credentials are not inherited by new users. Confirm a new author's choices, including whether book ideas may be treated as internalized values. Save private profiles separately from any public Git checkout.

## Optional skills

Use the current runtime's available-skill list to locate each skill's `SKILL.md`. Install only when the user asks; this project does not vendor or auto-install them.

| Capability | Optional skill |
|---|---|
| Long-form rhythm | `khazix-writer` |
| Chinese prose editing | `humanizer-zh` |
| Illustration planning | `baoyu-article-illustrator`, `ian-xiaohei-illustrations` |
| Raster generation | Runtime-native `imagegen` |
| Covers and HTML image cards | `guizang-social-card-skill`, `baoyu-cover-image` |
| Diagrams and infographics | `baoyu-diagram`, `baoyu-infographic` |
| WeChat typesetting | `gzh-design` (often stored under `gzh-design-skill`) |
| Zhihu typesetting | `md-zhihu-reflection-typesetting-skill` |
| Authorized platform delivery | `wechat-draft-push`, `zhihu-publisher`, `zhihu-mediacloud-uploader` |

Some integrations are local or environment-specific and may not have a public installer. There is no bundled browser, API client, publishing service, font or image-generation backend. If a dependency is unavailable, complete the supported local work and report the missing capability; do not promise a rendered image, uploaded draft or published article.

`md2wechat-skill` may be considered as an alternative only when actually installed and selected. The primary WeChat route in this workflow is `gzh-design`.

## Secrets and delivery records

Use the platform tool's documented secure credential mechanism. Do not commit tokens, session state, browser profiles, personal book notes, source chats or upload receipts. A previous successful delivery does not prove the current connection works. Check the current account and verify the new result.
