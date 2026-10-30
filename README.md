# Windowsill Essay Studio

**An author-specific essay skill—with the author's actual ideas and resources inside.**

这不是“帮使用者从零建立自己的风格”的通用写作框架，而是窗台作者本人的思想、声线与素材工作室。安装后即可读取内置内容，以作者的判断方式写完整观点长文；无需重新填写人设或投喂一套新资料。

## 已经放进去了什么

| 内容 | 实际位置 | 用法 |
|---|---|---|
| 16项作者判断及适用边界 | [worldview.md](resources/author/worldview.md) | 不是抽象风格标签，而是可发展的主张、理由与限制 |
| 作者声线、真实短表达锚点、审美与否定过的写法 | [voice.md](resources/author/voice.md) | 默认采用，不模仿其他作者的身份或经历 |
| 11张完整语境卡 | [学习](resources/contexts/learning.md)、[选择与兴趣](resources/contexts/choices.md) | 同时保留问题、作者判断、延伸与不能推导的结论 |
| 4组书籍思想综合 | [学习高手](resources/reading/learning.md)、[当下的力量](resources/reading/presence.md)、[马斯克原理](resources/reading/first-principles.md)、[Metaphors We Live By](resources/reading/metaphors.md) | 作者已授权内化；真正有内容，不只是列书名 |
| 8篇已有文章覆盖表 | [coverage.md](resources/articles/coverage.md) | 防止换标题重复，不把协作稿一律当最佳范文 |
| 只读检索脚本 | [search_resources.py](scripts/search_resources.py) | 检索随包正文；本机存在私有连接时同时查原材料 |

这里包含实际Markdown正文和清单，而不是只有“请学习作者风格”的提示词。内容语言主要是中文，名称与仓库标识为英文。

## 作者的几个判断

- 先看一条好建议替什么目标服务，再问它适不适合自己的生活。
- 分数证明完成某类考核，不自动等于会独立使用知识；基础和成绩也不能因此被否定。
- 抵触某个难题时，调整前置任务和练习难度，而不是给人贴“笨”的标签。
- 兴趣不必靠职业化来证明价值，但投入也要放回时间、资源和机会成本里看。
- AI降低产出成本，不会自动带来需求；兴趣练习与商业项目也不该共用唯一评分。

完整条件、反例与来源类型都在资源正文中。不要把这些判断再降格为“仅供使用者另建个人风格的示例”。

## Install

将仓库克隆到Codex技能目录下，目录名保持 `windowsill-essay-studio`。

```bash
git clone https://github.com/ljyhavefun-ai/windowsill-essay-studio.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/windowsill-essay-studio"
```

PowerShell:

```powershell
$root = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $HOME '.codex/skills' }
New-Item -ItemType Directory -Force -Path $root | Out-Null
git clone https://github.com/ljyhavefun-ai/windowsill-essay-studio.git (Join-Path $root 'windowsill-essay-studio')
```

已有安装先检查本机个性化文件，再更新；不要覆盖私人资料。刷新或新开Agent会话以发现Skill。检索脚本使用Python 3.10及以上标准库，无额外依赖。

## 直接使用

```text
使用 $windowsill-essay-studio，按窗台已有的思想与表达，写一篇关于
“学了很多却还是不能独立做事”的长文章。直接检索内置资源，只写稿。
```

```bash
python scripts/search_resources.py "兴趣 职业" --scope bundled --limit 5
python scripts/search_resources.py "退阶练习" --limit 4
python scripts/search_resources.py --stats
```

检索返回资源类别、文件、行号和匹配区域。原材料中的身份与条件仍要按[资源规则](references/resource-use.md)核对，不能只凭命中半句话写作。

## 本机原材料与公开内容的区别

- **任何安装都可用**：随包的作者思想、声线、匿名语境、书籍短综合与文章覆盖表。
- **作者本机增强**：`private/sources.json` 直接连接已存在的聊天整理全文、知乎旧作、项目文章和Obsidian笔记；auto模式自动读取，不重新索要资料。
- **不公开分发**：原始私聊、第三方身份、书籍全文、个人目录和账号凭据。公开思想内容与把私人原件全部开源不是一回事。

本机安装版保留私人连接；GitHub安装版没有访问作者电脑的能力，也不声称读过其全部书库。它仍然能使用已装入的内容写稿，不能把资源缺失作为重新塑造调用者风格的理由。以原作者视角写作不等于让调用者冒充他的真实人生。

## 完整创作链路

资源检索与语境理解 → 观点和反例 → 长文母稿 → 自然表达编辑 → 原创插图与HTML文字图 → 平台排版 → 授权范围内推送与回读。

### 热点与知乎深答

已融合作者此前两份知乎高赞长文Skill：生活关联与认知缺口、事实／陈述／未知分层、现象—机制—代价／替代分析、最强反方，以及来自实际取舍的结尾问题。详见[知乎长文方法](references/zhihu-longform.md)。

它与内置作者资源共用一套人格和判断，不是复制两个新入口。固定六段、每千字金句、延迟简单答案、引用框代替所有加粗等旧规则已改为按内容和平台选择；不许诺高赞、完读或涨粉，不为制造争论牺牲事实与作者立场。

### 从实稿失败补上的质量检查

[证据与一致性检查](references/quality-gates.md)处理检索残留、个例泛化、不可比数据推因果、修辞充当证明、方案默认有余量，以及正文与来源记录互相矛盾等问题。写作前绑定主读者，成文后从最终正文反查证据与规则；不会把来源名气当代表性，也不以格式通过代替内容正确。

回归用例只提供[构造的错误片段](tests/fixtures/quality-cases.json)，不公开真实评审原稿或内部来源记录。它们用于验证具体判断，不是词语黑名单或自动评分器。

专项Skills按需提供技术能力，不会取代内置作者内容。见[依赖与连接](references/local-environment.md)和[第三方说明](THIRD_PARTY.md)。未捆绑任何第三方完整实现、浏览器、排版引擎或生图后端。

- 公众号默认进草稿箱，不冒称公开发布或群发。
- 知乎按指定问题／文章和草稿／公开范围执行并核验。
- 小红书只交付无空行TXT和本地图片，用户手动上传，不自动操作后台。
- 排版保持定稿文字；语言编辑与内容适配另存版本。
- 不编造经历、数字、完成状态或读书程度，不承诺流量或通过AI检测。

## License

本项目原创工作流、作者内容整理及检索代码采用[MIT许可证](LICENSE)。第三方Skill及原书著作权不因本仓库开源而改变；书籍资源仅为重新组织的短篇思想综合，不是原书或笔记全文。
