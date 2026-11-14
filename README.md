# 🚀 Space Mission Design Game: Lunar South Pole Water-Ice Explorer
**2026 NASA Space Apps Challenge — Space Mission Design Game**

> **体验真实的航天系统工程权衡（System Engineering Trade-offs）：** 从运载火箭选型、六大子系统组装、奔月轨道转移到月球南极永夜区着陆与光谱研判，用你的工程决策揭开月球水冰的秘密。

[🌐 Live Demo (在线试玩)](#) · [🎬 30s Demo Video (演示视频)](#) · [📚 NASA Data References (数据基准)](#-nasa-data-references--physics-mapping)

---

## 📖 1. 项目愿景与核心痛点 (Project Vision)

在传统的航天科普与教学中，学习者往往只能接触孤立的概念（如单一轨道公式或火箭推力），缺乏将**科学目标、工程约束、资源预算与任务运营**串联起来的全局系统工程体验[cite: 1]。

**Space Mission Design Game** 旨在填补这一断层[cite: 1]。我们以真实前沿任务 **《寻找月球水冰：南极探测任务》** 为首个剧本[cite: 2, 4]，让玩家化身任务总师，在有限的资源池中做出取舍——**没有唯一的“标准答案”**，无论是低成本商业火箭搭配轻量化载荷，还是重型火箭搭载高精尖光谱仪，只要经受住物理逻辑与资源约束的考验，都能抵达月球南极[cite: 1, 2]。

---

## ⚖️ 2. 核心工程权衡机制 (Core Engineering Trade-offs)

游戏中任何一项设计变更都会产生“牵一发而动全身”的连锁反应[cite: 1]。系统围绕 NASA 任务设计规范构建了 **六大核心资源动态约束**[cite: 1]：

| 核心资源 | 系统约束与工程博弈逻辑 | 交互表现形式 |
| :--- | :--- | :--- |
| **💰 预算 (Budget)** | 覆盖运载火箭发射费与六大航天器子系统采购成本。 | **硬性门控 (Hard Gate)**：预算超支时发射按钮直接锁死[cite: 2]。 |
| **⚖️ 质量 (Mass)** | 航天器总质量需匹配所选火箭的奔月转移（TLI）运力上限[cite: 2]。 | **软性风险 (Soft Gate)**：允许超重强行点火，但会在后续转移或着陆阶段引发推力不足失败并给出物理归因[cite: 2]。 |
| **⚡ 电力 (Power)** | 太阳能板发电功率 + 电池储能需覆盖仪器工作与极寒保温功耗[cite: 2, 3]。 | 实时动态演算，阴影区断电将导致仪器停机或热控失效[cite: 2]。 |
| **📡 通信 (Comms)** | 天线增益与地面站窗口决定地月遥测与科学数据下传速率[cite: 1]。 | 带宽不足将造成数据积压丢失，影响最终科学评分[cite: 1]。 |
| **📊 数据 (Data)** | 高分辨率光谱/中子仪器产生海量数据，受限于存储与带宽[cite: 1]。 | 需在“高精尖数据”与“传输瓶颈”之间寻找平衡点[cite: 1]。 |
| **⏳ 寿命 (Lifetime)** | 受着陆策略燃料消耗、电池循环及极寒环境耐受度共同制约[cite: 1, 2]。 | 决定月面有效科学探测窗口时长[cite: 1]。 |

---

## 🎮 3. 游戏核心流程：五幕闭环体验 (5-Act Gameplay Loop)

为了明确区分 **“玩家主动工程决策”** 与 **“系统自动物理演算”**[cite: 2, 3]，游戏采用递进式五幕架构：

### 🔹 第 0 幕：主视觉与任务简报 (Home & Mission Briefing)
* **航天极简 HUD**：深空背景（`#060913`）搭配带有南极光晕的 2D 矢量月球与粗犷工业风全大写标题[cite: 2, 3]。
* **5 分钟极速上手**：横向任务轮播切换剧本，内置 **≤120 字的“3 卡片微科普弹窗（How to Play）”**，零门槛讲解水冰探测目标、三大资源权衡与“假阳性陷阱”[cite: 2, 3]。

### 🔹 第 1 幕：运载火箭选型 (Launch Vehicle Selection)
* 通过 Coverflow 卡片对比多款现役与前沿运载火箭（如 *Falcon 9*、*Vulcan Centaur*、*SLS Block 1*）的 **奔月转移（TLI）有效载荷上限** 与 **发射成本**[cite: 2]，锁定初始任务包络。

### 🔹 第 2 幕：六步航天器模块化组装 (Modular Spacecraft Assembly)
* 遵循**希克定律（Hick's Law）**，玩家按以下顺序逐步装配探测器，每步同屏仅展示 3–4 个高对比度组件卡片，右侧实时点亮 CAD 蓝图与遥测资源条（`< 200ms` 响应）[cite: 2, 3]：
  1. `Platform`（探测器平台）[cite: 2]
  2. `Structure`（承力与热控结构）[cite: 2]
  3. `Solar Panel`（太阳能帆板）[cite: 2]
  4. `Battery`（深空蓄电池）[cite: 2]
  5. `Antenna`（高增益通信天线）[cite: 2]
  6. `Scientific Instrument`（科学探测载荷：中子谱仪、近红外光谱仪等）[cite: 2]

### 🔹 第 3 幕：奔月转移与南极 3D 交互着陆 (Launch, Transfer & 3D Landing)
* **双重发射门控**：起飞前总览页检查预算（硬性锁死）与总质量（超重警告但允许冒险起飞）[cite: 2]。
* **遥测慢动作过场**：全屏演示 *离地升空 → 地月转移 → 近月制动* 三阶段轨迹，伴随适速打字机终端实时播报能源与热控状态[cite: 2, 5]。
* **3D 半月轨道选址与着陆**：自由旋转缩放 3D 月球模型，在 **沙克尔顿陨石坑（Shackleton）、诺比莱边缘（Nobile Rim）、卡比厄斯（Cabeus）、马拉珀特山（Malapert）** 间选定着陆区并设定着陆策略（省燃料 / 标准 / 安全优先），随后通过 3D PBR 写实着陆动画演绎软着陆或坡度受损结局[cite: 2, 5]。

### 🔹 第 4 幕：科学图谱研判与工程复盘 (Science Analysis & Debrief)
* **破解“假阳性陷阱”**：玩家需亲自分析下传的光谱与中子计数图谱，区分 **真实水冰信号** 与 **月表羟基（OH）干扰陷阱**[cite: 2, 3]。
* **多维评分与零惩罚迭代**：系统生成五边形能力雷达图与明确的物理成败归因，支持 **一键返回指定组装步骤微调参数** 再次挑战[cite: 2, 3]。

---

## 🤝 4. 单人及 4 人团队协作模式 (Single-Player & 4-Player Co-op)

紧扣官方团队协作设计要求，支持 **单人独立统筹** 或 **最多 4 人联机/同屏协同**[cite: 1]：
1. **任务总师 (Mission Planner)**：把控全局预算、任务目标与最终发射决策[cite: 1]。
2. **结构与动力工程师 (Spacecraft & Power)**：负责平台、结构、帆板与电池的重量与发电配平[cite: 1, 2]。
3. **通信与轨道专家 (Comms & Orbit)**：规划轨道路径、天线增益与南极着陆点选址[cite: 1, 2]。
4. **首席科学家 (Payload & Science)**：选配科学仪器并在最终阶段负责光谱图谱真伪研判[cite: 1, 2]。

---

## 🎨 5. 设计哲学与交互规范 (UI/UX Design Philosophy)

* **Aerospace Minimalism（航天极简主义）**：严格保留 **45%–55% 黄金留白**，拒绝信息堆砌，营造沉浸式深空控制中心氛围[cite: 3]。
* **等宽遥测数字（Tabular Monospace）**：所有动态跳动的预算、重量、功率数值均采用等宽字体，杜绝数值刷新时的视觉抖动[cite: 3]。
* **科普友好微文案（Microcopy）**：专业术语（如 *PSR 永久阴影区*、*TLI 奔月运力*）首次出现时均附带 `≤8 字` 的通俗白话注解，确保青少年与非专业玩家无障碍游玩[cite: 3]。

---

## 🛰️ 6. NASA 官方数据来源与物理依据 (NASA Data References)

游戏内所有运载火箭运力、子系统能耗比及月球南极地形光照参数均映射自 NASA 公开任务基准数据[cite: 1, 4]：

* **运载火箭性能参数**：参考 *NASA Space Launch System (SLS) Fact Sheets* 及 *NASA Launch Services Program (LSP)* 公开奔月转移（TLI）载荷能力基准。
* **月球南极着陆区地形与光照**：参考 *Lunar Reconnaissance Orbiter (LRO)* 搭载的 **LOLA（月球轨道器激光高度计）** 与 **Diviner（月球辐射计实验）** 永久阴影区（PSR）温度分布数据。
* **水冰与羟基光谱探测模型**：参考 *LCROSS（月球陨坑观测和传感卫星）* 撞击数据、*LRO LEND（月球探索中子探测器）* 氢丰度数据及 *NASA VIPER（月球极地挥发物调查漫游车）* 载荷设计指标。

---

## 🛠️ 7. 技术栈与项目结构 (Tech Stack & Architecture)

* **前端框架**：React / TypeScript / Vite
* **样式与动效**：Tailwind CSS / Framer Motion（`< 200ms` 交互反馈与 HUD 遥测过渡）[cite: 3]
* **3D 渲染与可视化**：Three.js（月球南极 3D 选址与着陆演算）[cite: 5] / Custom SVG & Canvas（航天器动态蓝图与光谱图表）[cite: 2]

```text
space-mission-design-game/
├── public/
│   └── assets/               # 2D 矢量星球、3D 月球纹理与音效资源
├── src/
│   ├── components/
│   │   ├── act0-briefing/    # 第 0 幕：主界面 HUD 与三卡片微科普弹窗
│   │   ├── act1-launcher/    # 第 1 幕：运载火箭 Coverflow 选型器
│   │   ├── act2-assembly/    # 第 2 幕：六步子系统组装台与实时 CAD 蓝图
│   │   ├── act3-flight/      # 第 3 幕：双重发射门控、慢动作转移过场与 3D 南极着陆
│   │   └── act4-debrief/     # 第 4 幕：光谱真伪研判器、五边形雷达图与复盘报告
│   ├── data/
│   │   └── missionDatabase.ts # 火箭、子系统、着陆区参数及 NASA 引用字典
│   ├── engine/
│   │   └── physicsValidator.ts # 资源联动演算、超重/断电失效归因引擎
│   └── styles/
│       └── tokens.css        # 航天极简深空色彩与等宽字体 Design Tokens
└── README.md
