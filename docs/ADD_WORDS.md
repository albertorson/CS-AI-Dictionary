# 快速教程：新增或修改词条

[返回首页](../README.md) · [完整贡献规范](../CONTRIBUTING.md)

1. 获取仓库，在 `data/community/` 新建 UTF-8 文件，例如 `my_ai_terms.jsonl`。复制 [词条模板](../examples/entry.jsonl) 并替换为真实内容；每行一个完整 JSON 对象，不要把一个对象拆成多行。文件名不要求固定前缀。
2. 填写词头、词性、领域、中文核心释义、专业释义、语境、搭配、例句与辨析；音标可选。领域使用贡献指南列出的七个英文值之一。新词不需要填写 status 或 batch。
3. 修改已有词时，先搜索它所在的 JSON/JSONL，再修改原记录，不要另加同名词。不要直接编辑 TXT 或 `.eudic`，下一次构建会从源数据重新生成内容。
4. 在仓库根目录运行：

```bash
# 检查全部词条及两版渲染；没有固定词数限制
python build.py --check
# 运行扩展、重复词、缺失字段等测试
python -m unittest discover -s tests
# 生成本地 TXT 与 HTML，供检查和打包
python build.py
```

5. 若只为自己使用，按 [打包教程](BUILD.md) 制作 `.eudic` 即可。若希望贡献给项目，Fork 后提交 PR，附上改动说明、参考来源与 AI 辅助情况，等待维护者审核。

使用 Agent 辅助编写时，也应让它修改源数据、检查重复词，并人工核实定义及例句。自动检查只验证结构和可构建性，不证明专业内容正确。数据提交不会自动重新编译现有 `.eudic`。
