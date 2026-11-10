# 贡献指南

欢迎新增词条、纠正释义、补充例句。Python 3.10 或以上即可，无需安装第三方依赖。

1. Fork 本仓库并创建自己的分支。
2. 新词放入 `data/community/任意描述性名称.jsonl`，每行一个 JSON 对象。复制 `examples/entry.jsonl` 的结构并替换所有内容；示例不自动参与构建。
3. 修改已有词条时，搜索其 word 并直接修改原记录，不另建同名条目。不要重复录入词头（大小写、首尾及连续空格会归一化）。
4. 运行 `python build.py --check`，再运行 `python -m unittest discover -s tests`。
5. 提交 Pull Request，说明词条用途、参考来源及 AI 辅助情况。审核通过后由维护者合并。

## 数据要求

必填字段：word、pos、domain、core、definition、contexts、collocations、examples、distinction。ipa 可选；status 和 batch 可省略，新增条目自动设置。不要为新词填写 preserved。

contexts 为 1–4 组 scene/translation/note；collocations 为 3–5 组 en/zh；examples 为 1–3 组 en/zh。新词 definition 至少 20 字符，distinction 至少 10 字符。中文字段应包含中文。格式检查不能保证释义事实正确，仍需人工审阅。

domain 必须使用 dictionary_config.json 的 domains 中的标识。当前预设为：

- Programming & Algorithms
- Software Engineering & Git
- Operating Systems & Linux
- Computer Networks
- Databases & Distributed Systems
- AI & Machine Learning
- Developer Tools & Environment

增加领域时，在 dictionary_config.json 的 domains 中添加标识及中文显示名，并在 PR 中说明分类依据；无需改 Python 代码。没有固定词数或领域配额。

## 构建与发布

`python build.py` 从同一份数据生成两版 TXT、增强版 HTML 和 statistics.json，均写入忽略上传的 local_output。不要直接编辑生成 TXT，也不要提交 TXT、HTML 或 CSV。

CSV 只是可选的表格镜像：`python export_csv_mirror.py`。不需要 CSV 就不运行它。

欧路 .eudic 编译仍需维护者在本地使用欧路构建器，分别选择生成的两个 TXT。仓库内现有 .eudic 是 v1.1 的 3000 词快照，不会随数据提交自动改变。发布前应人工导入欧路检查显示和查词，后续版本可通过 Releases 发布 .eudic。

提交贡献表示你有权按仓库 LICENSE（CC BY-NC-SA 4.0）提供相关内容。请勿复制无再分发授权的商业词典释义。
