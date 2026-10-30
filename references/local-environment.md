# Existing Resources and Optional Dependencies

本Skill已经内置窗台作者的思想、声线、语境和读书综合，不是等待使用者重新建立风格的空架子。直接使用 `resources` 中的正文；`resources/manifest.json` 是清单，`references/resource-use.md` 说明检索方法。

## 本机既有资料连接

作者本机安装版使用 `private/sources.json` 连接已整理的聊天全文、旧知乎文章、八篇项目稿件及Obsidian阅读笔记。运行 `scripts/search_resources.py` 的默认auto模式会自动使用这份连接；不需要重新提供路径。该配置只保存在本机，已被Git忽略，不含凭据。

公开安装版没有私人目录访问权，但真正随包提供了作者内容，因此仍能直接检索和写作。不要假称访问了私人全文，不要求下载者为了使用本作者风格先配置自己的书库、思想或人设。需要进一步原文核对时说明该层资源是否可访问。

本机连接只读取已登记的Markdown和TXT文件；目录是否递归由配置声明，不扫描整盘，不修改资料，不进行网络请求。缺路径报告警告，并继续使用可读的内置资源。

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
