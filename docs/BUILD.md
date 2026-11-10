# 制作教程：从源数据生成欧路词典

[返回首页](../README.md) · [安装成品](INSTALL.md) · [新增词条](ADD_WORDS.md)

本教程适用于想把自己的词条打包进欧路词典的用户。数据生成需要 Python 3.10+；下文的 EuDicBuilder 打包步骤面向 Windows。

## 1. 先认清文件

```text
JSON/JSONL 源数据 → python build.py → 两个 TXT → EuDicBuilder → 两个 .eudic
```

本项目生成的是欧路自定义格式的 **TXT，不是 TSV**。每个词条占一行，词头与 HTML 释义之间用 `@` 分隔。TSV 使用制表符分隔，不能仅改后缀来替代。仓库的 existing_headwords.tsv 只是旧版词头清单，不含完整释义，不能用于制作这两个词典。

格式依据：[欧路官方词库制作工具与文本格式说明](https://www.eudic.net/v4/en/home/EudicBuilder)。

## 2. 获取项目并生成 TXT

在 GitHub 仓库点 Code → Download ZIP 并解压，或使用自己的 Git 副本。打开项目文件夹中的终端，确认能看到 build.py。以下命令在该目录运行：

```powershell
# 查看 Python 版本，应为 3.10 或以上
python --version

# 检查字段、重复词头和两版输出结构，不写文件
python build.py --check

# 根据全部词条生成两版 TXT 和预览
python build.py
```

如提示找不到 python，请安装 Python 并重新打开终端，或使用本机实际的 Python 路径。无需安装额外 Python 包。

成功后，打开 `local_output`，找到：

| 文件 | 用途 |
|---|---|
| CS_AI_Dictionary_Simple_v1.1_EudicBuilder.txt | 简洁版打包输入 |
| CS_AI_Dictionary_Extended_v1.1_EudicBuilder.txt | 增强版打包输入 |
| CS_AI_Dictionary_Extended_v1.1_preview.html | 浏览器中预览增强版 |
| statistics.json | 本次数据总数与领域统计 |

文件名中的 v1.1 是目前脚本保留的兼容命名，内容来自本次读取的全部数据，并非只能包含旧版 3000 词。可以打开 HTML 检查刚添加的词；浏览器预览不能替代欧路中的显示检查。

## 3. 使用欧路构建器

1. 从上面的欧路官方页面下载“欧路词典的词库制作工具”，解压后运行 EuDicBuilder.exe。它不是同页的 MdxBuilder，后者用于另一种格式。
2. 在源文件选择项中，选择刚生成的简洁版 TXT。若工具要求选择格式，使用自定义文本格式。
3. 填写工具提供的词库名称、作者等信息。建议名称包含版本和“简洁版”，例如 `CS-AI 简洁版（个人更新版）`。
4. 若有“资源目录”选项，本项目当前词条没有外置图片或声音，可以留空。README 的图床图片无需放入词典资源目录。
5. 设置工具允许指定的输出位置，执行生成/压缩。不同工具版本字段和按钮名称可能不同，以工具附带说明为准。
6. 完成后找到输出的 `.eudic` 文件，取一个能区分版本的名字，例如 `CS-AI-Simple-custom.eudic`。
7. 用增强版 TXT 重复一次，将词库名称与输出文件名改为增强版，避免覆盖简洁版。

不要把 CSV、HTML 预览或 JSONL 直接作为构建器输入；不要通过重命名 TXT 后缀来伪造 `.eudic`。本仓库不分发第三方构建器，也没有自动执行 `.eudic` 编译。

## 4. 验证并使用成品

按 [安装教程](INSTALL.md) 导入新的 `.eudic`。至少查一个原有词和一个新增词，检查中文、例句、增强版折叠及两个版本是否都能查到。若显示的仍是旧内容，检查是否打包了新的 local_output/TXT，以及客户端是否仍启用了旧词库。

TXT、HTML、CSV 为本地生成产物，不提交 GitHub。当前根目录里的两个 v1.1 `.eudic` 不会被脚本覆盖；发布新成品时可通过 GitHub Releases 附件提供 `.eudic`。修改和分享须遵守项目 LICENSE。
