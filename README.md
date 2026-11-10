# CS-AI Dictionary

面向计算机科学与人工智能学习的英汉技术词典，可直接导入欧路词典使用。

词典v1.1版共收录 **3000 个技术词条**，覆盖人工智能、程序设计、软件工程、数据库、计算机网络、操作系统与开发工具等领域。

项目现已支持持续扩展，3000 是 v1.1 成品的词数，并非上限。欢迎按照 [贡献指南](CONTRIBUTING.md) 新增词条或纠错。每次推送和 Pull Request 会自动检查数据并尝试生成两个版本。

## 词典版本

| 版本 | 特点 | 适合场景 |
|---|---|---|
| 简洁版 | 中文释义、词性、专业释义、场景辨析、例句 | 快速查词 |
| 增强版 | 语境、常见搭配、双语例句、易混词辨析 | 深入学习和专业阅读 |

<p align="center">
<img width="1013" height="322" alt="image" src="https://github.com/user-attachments/assets/79f7eb83-6eb9-481a-9909-dd58a74674b4" />
<br>
<em>简洁版示例</em>
</p>

<p align="center">
<img width="971" height="604" alt="image" src="https://github.com/user-attachments/assets/3e99ed24-916a-4a71-98b1-eb348625afd7" />
<br>
<em>增强版示例（折叠）</em>
</p>

<p align="center">
<img width="992" height="946" alt="image" src="https://github.com/user-attachments/assets/39a48f69-8573-4826-b7c8-e90d3dbc2a24" />
<br>
<em>增强版示例（展开）</em>
</p>


## 词条覆盖

| 领域 | 词条数 |
|---|---:|
| 人工智能与机器学习 | 550 |
| 软件工程与 Git | 550 |
| 程序设计与算法 | 500 |
| 操作系统与 Linux | 450 |
| 计算机网络 | 350 |
| 数据库与分布式系统 | 350 |
| 开发工具与环境 | 250 |
| **合计** | **3000** |

## 下载

- [下载简洁版](CS_AI_Dictionary_Simple_v1.1_EudicBuilder.eudic)
- [下载增强版](CS_AI_Dictionary_Extended_v1.1_EudicBuilder.eudic)

下载 `.eudic` 文件后，在欧路词典中导入即可使用。

## 使用教程

- **只想使用词典：**[下载、安装到欧路词典并开始查词](docs/INSTALL.md)
- **想自己制作成品：**[把脚本生成的 TXT 打包为 .eudic](docs/BUILD.md)
- **想扩充内容：**[快速新增或修改词条](docs/ADD_WORDS.md)

目前构建输出为欧路专用 TXT（不是 TSV）；详细格式要求和社区协作流程见 [贡献指南](CONTRIBUTING.md)。

## 数据与构建

词典的源数据位于：

```text
extended_data/v1.1/
```

其中：

- `base_v1.0.json`：最初的 300 条词条；
- `additions/*.jsonl`：后续增加的 2700 条词条；
- `build_extended_dictionary.py`：生成增强版；
- `build_simple_dictionary.py`：生成简洁版。

JSON/JSONL 是词典的主要数据源，TXT 和 `.eudic` 是生成产物。

社区新增词条放入 `data/community/*.jsonl`。保留旧数据路径是为了兼容现有内容，不代表数据只能用于 v1.1。

需要 Python 3.10+，无需第三方依赖：

```bash
# 只检查数据及两版能否生成，不写文件
python build.py --check
# 生成两版 TXT、HTML 预览及动态统计，均仅存于 local_output
python build.py
```

TXT、HTML、CSV 不上传 GitHub。CSV 仅为可选的表格镜像，普通贡献者无需使用。网页表格与下载的 `.eudic` 当前仍对应 v1.1；新词提交不会自动更新二进制成品，维护者需要用欧路构建器重新打包。

## 项目说明

本项目是社区制作的自定义词典，与欧路软件及其开发者不存在隶属或官方合作关系。“欧路词典”等名称和标识归相应权利人所有。

## 许可证

除另有说明外，本仓库内容采用 [CC BY-NC-SA 4.0](LICENSE)，署名 albertorson 并链接本项目；分享时注明修改，改编后分享须遵守相同方式共享条款，仅许可非商业用途。商业使用需另行获得授权。
