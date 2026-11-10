# -*- coding: utf-8 -*-
"""按批次文件统计条数并生成批次覆盖日志（条数自动，覆盖说明人工维护）。"""
from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ADD = ROOT / "extended_data" / "v1.1" / "additions"
OUT = ROOT / "BATCH_LOG_v1.1.md"

DOMAIN_OF_PREFIX = {
    "programming": "程序设计与算法",
    "software": "软件工程与 Git",
    "os": "操作系统与 Linux",
    "net": "计算机网络",
    "db": "数据库与分布式系统",
    "ai": "人工智能与机器学习",
    "dev": "开发工具与环境",
}

COVERAGE = {
    "programming_01": "编程基础：变量、类型、控制流、函数与基础数据结构",
    "programming_02": "数据结构与算法：数组、链表、树、堆、哈希与复杂度",
    "programming_03": "算法范式：递归、分治、动态规划、贪心与图算法",
    "programming_04": "进阶编程：迭代器、并发原语、设计模式与语言特性",
    "software_01": "软件工程基础：需求、设计原则、代码质量与评审",
    "software_02": "Git 与版本控制：提交、分支、历史与协作",
    "software_03": "协作流程：代码评审、测试策略、敏捷与文档",
    "software_04a": "架构与设计：模块边界、接口与架构风格",
    "software_04b": "软件维护：技术债、重构、配置与发布实践",
    "os_01a": "操作系统基础：进程、内核与系统调用",
    "os_01b": "进程与线程：调度、上下文切换与同步",
    "os_02b": "内存管理：虚拟内存、分页与置换",
    "os_03": "文件系统与 I/O：文件、目录、权限与设备",
    "os_04": "Linux 系统：命令、服务、信号与系统管理",
    "os_05a": "Linux 运维：作业控制、定时任务与网络工具",
    "os_05b": "系统资源：磁盘、进程查看与性能基础",
    "os_05c": "Shell 与脚本：环境变量、通配与文本处理",
    "net_01": "网络模型与基础：分层、协议、地址与端口",
    "net_02": "链路与网络层：以太网、IP、路由与 ICMP",
    "net_03": "传输层：TCP、UDP、握手、流控与拥塞",
    "net_04": "应用层：HTTP、HTTPS、DNS 与常见协议",
    "net_05": "Web 与网络安全：TLS、代理、Cookie 与攻击面",
    "net_06": "网络工程：NAT、VPN、负载均衡与诊断",
    "net_07": "网络补充：现代协议与术语凑批",
    "db_01": "关系模型与 SQL：表、键、约束与基础查询",
    "db_02": "数据库设计：范式、关系、ER 与建模",
    "db_03": "索引：B 树、复合索引、覆盖与执行计划",
    "db_04": "查询优化：优化器、统计信息、重写与计划",
    "db_05": "事务与并发：锁、MVCC、隔离级别与死锁",
    "db_06": "MySQL/PostgreSQL：引擎、方言、复制与运维",
    "db_07": "Redis 与缓存：数据结构、过期、淘汰与缓存模式",
    "db_08": "NoSQL：文档、列式、宽列与图数据库",
    "db_09": "分布式：分片、复制、一致性、共识与 CAP",
    "db_10": "数仓与流：ETL、消息队列、Kafka 与数据湖",
    "ai_01": "机器学习基础：监督、无监督、评估与指标",
    "ai_02": "模型与训练：回归、分类、正则与验证",
    "ai_03": "深度学习：神经网络、激活、优化与初始化",
    "ai_04": "序列与网络：CNN、RNN、序列建模与正则",
    "ai_05": "NLP 基础：语言模型、采样、注意力与文本处理",
    "ai_06": "提示工程与上下文管理：模板、注入、压缩与评测",
    "ai_07": "RAG 与检索：分块、向量索引、混合检索与评估",
    "ai_08": "Agent 与 MCP：工具调用、代理循环、记忆与框架",
    "ai_09": "强化学习与对齐：RLHF、DPO、RL 基础与可解释",
    "ai_10": "多模态与推理服务：VLM、语音、vLLM、量化与部署",
    "ai_11": "配额凑批：指令遵循、数据治理与安全过滤",
    "dev_01": "编辑器与托管：VS Code、JetBrains、GitHub 与界面",
    "dev_02": "命令行与远程：Shell、SSH、WSL、scp 与配置",
    "dev_03": "包管理与容器：npm、pip、conda、Docker 与 K8s",
    "dev_04": "CI/CD 与云：管道、特性开关、Terraform、监控",
    "dev_05": "调试与质量：断点、单步、性能分析、测试与界面动词",
    "dev_06": "生态工具：终端、构建、可观测、安全与本地集群",
}


def count_lines(path: Path) -> int:
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def main() -> None:
    groups: OrderedDict[str, list[tuple[str, int]]] = OrderedDict()
    for path in sorted(ADD.glob("*.jsonl")):
        prefix = path.stem.split("_")[0]
        domain = DOMAIN_OF_PREFIX[prefix]
        groups.setdefault(domain, []).append((path.stem, count_lines(path)))

    total = 0
    parts = [
        "# CS-AI 技术词典 v1.1 批次日志",
        "",
        "- 主数据：`extended_data/v1.1/base_v1.0.json`（300 条 preserved）+ `additions/*.jsonl`",
        "- 本日志条数由脚本自动统计；覆盖范围为人工记录",
        "- 同步产物：欧路 TXT、预览 HTML、可编辑 CSV 镜像",
        "",
        "## 基线（v1.0 保留）",
        "",
        "| 来源 | 条数 |",
        "|---|---|",
        "| base_v1.0.json | 300 |",
        "",
        "## 新增批次",
        "",
    ]
    for domain, batches in groups.items():
        subtotal = sum(n for _, n in batches)
        total += subtotal
        parts.append(f"### {domain}（新增 {subtotal} 条）")
        parts.append("")
        parts.append("| 批次文件 | 条数 | 覆盖范围 |")
        parts.append("|---|---|---|")
        for stem, n in batches:
            parts.append(f"| {stem} | {n} | {COVERAGE.get(stem, '')} |")
        parts.append("")
    parts.append(f"## 汇总")
    parts.append("")
    parts.append(f"- 新增词条：{total} 条")
    parts.append(f"- 保留词条：300 条")
    parts.append(f"- 全库总计：{total + 300} 条")
    parts.append("")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"新增 {total}，总计 {total + 300}，日志：{OUT}")


def current_report():
    """历史批次日志保持不变，当前统计从全部数据动态生成。"""
    from build_extended_dictionary import load_entries, validate_entries, LOCAL_OUTPUT, DOMAIN_ZH
    entries, _ = load_entries()
    counts = validate_entries(entries)
    LOCAL_OUTPUT.mkdir(exist_ok=True)
    lines = ['# 当前词典统计', '', f'总词条：{len(entries)}', '', '| 领域 | 数量 |', '|---|---:|']
    lines.extend(f'| {DOMAIN_ZH[d]} | {counts[d]} |' for d in DOMAIN_ZH)
    destination = LOCAL_OUTPUT / 'STATISTICS.md'
    destination.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'已生成动态统计：{destination}')


if __name__ == "__main__":
    current_report()
