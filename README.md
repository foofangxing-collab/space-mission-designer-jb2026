# 🚀 Space Mission Design Game:
**2026 NASA Space Apps Challenge — Space Mission Design Game**

> **Experience authentic aerospace system engineering trade-offs:** From launch vehicle selection, six-subsystem spacecraft assembly, and trans-lunar injection to 3D Lunar South Pole landing and spectral data verification—use your engineering judgment to uncover the truth behind lunar water ice.

[🌐 Live Demo](#) · [🎬 30s Demo Video](#) · [📚 NASA Data References](#-6-nasa-data-references--physics-mapping)

---

## 📖 1. Project Vision & Core Problem

In traditional space science education, learners often encounter isolated concepts—such as a single orbital equation or rocket thrust formula—without experiencing how **science objectives, engineering constraints, resource budgets, and mission operations** interlock in a real spaceflight program.

**Space Mission Design Game** bridges this gap. Centered on a cutting-edge mission scenario—**"Hunting Lunar Water Ice: South Pole Exploration"**—players take on the role of Chief Mission Designer to balance competing constraints within a finite resource pool[cite: 2]. **There is no single "correct" solution:** whether you pair a cost-effective commercial launcher with a lightweight payload or deploy a heavy-lift rocket carrying high-precision spectrometers, any architecture that survives physics validation and resource limits can reach the lunar south pole.

---

## ⚖️ 2. Core Engineering Trade-offs

Every design choice triggers cascading system-wide consequences. The simulation models **six interconnected resource constraints** grounded in NASA mission engineering principles:

| Core Resource | System Constraint & Engineering Trade-off | Interactive Behavior |
| :--- | :--- | :--- |
| **💰 Budget** | Covers launch vehicle procurement and all six spacecraft subsystems. | **Hard Gate**: Exceeding the budget locks the launch button immediately. |
| **⚖️ Mass** | Total spacecraft wet/dry mass must fit within the selected rocket's Trans-Lunar Injection (TLI) payload capacity. | **Soft Risk Gate**: Overweight launches are permitted with warnings, but trigger thrust-deficit or propellant-depletion failures during transfer or landing with clear physical root-cause feedback. |
| **⚡ Power** | Solar array generation and battery storage must sustain scientific instruments and cryogenic thermal survival. | Calculated dynamically in real time; power deficits in shadowed zones cause instrument shutdown or thermal failure. |
| **📡 Comms** | Antenna gain and ground station windows govern Earth-Moon telemetry and science downlink rates. | Insufficient bandwidth causes data bottlenecks and packet loss, lowering the final science score. |
| **📊 Data** | High-resolution neutron and infrared spectrometers generate massive datasets constrained by storage and downlink. | Forces players to balance high-fidelity science return against transmission bottlenecks. |
| **⏳ Lifetime** | Governed by landing propellant margins, battery charge cycles, and extreme cryogenic endurance. | Determines the active operational window on the lunar surface. |

---

## 🎮 3. Gameplay Loop: 5-Act Architecture

To clearly distinguish **active player engineering decisions** from **automated physics simulations** and **cinematic telemetry transitions**[cite: 1], the game is structured into five progressive acts:

### 🔹 Act 0: Home HUD & Mission Briefing
* **Aerospace Minimalism HUD**: Deep-space canvas (`#060913`) paired with a 2D vector Moon featuring a South Pole glow and industrial uppercase typography.
* **5-Minute Onboarding**: A horizontal mission carousel introduces the scenario alongside a **≤120-word "3-Card Micro-Tutorial (How to Play)"** that explains the water-ice objective, core resource trade-offs, and the "false-positive trap."

### 🔹 Act 1: Launch Vehicle Selection
* Players compare real-world launch vehicles (such as *Falcon 9*, *Vulcan Centaur*, and *SLS Block 1*) via an interactive Coverflow selector, weighing **Trans-Lunar Injection (TLI) payload capacity** against **launch cost** to establish the mission's physical envelope[cite: 2].

### 🔹 Act 2: Six-Step Modular Spacecraft Assembly
* Designed around **Hick's Law**, players assemble their spacecraft sequentially across six subsystems[cite: 2]. Each step displays only 3–4 high-contrast component cards while dynamically illuminating a live CAD blueprint and telemetry bars (`< 200ms` response):
  1. `Platform` (Spacecraft Bus)[cite: 2]
  2. `Structure` (Primary Load-Bearing & Thermal Structure)[cite: 2]
  3. `Solar Panel` (Photovoltaic Arrays)[cite: 2]
  4. `Battery` (Deep-Space Energy Storage)[cite: 2]
  5. `Antenna` (High-Gain Communications)[cite: 2]
  6. `Scientific Instrument` (Neutron Spectrometer, Near-Infrared Spectrometer, etc.)[cite: 2]

### 🔹 Act 3: Launch, Transfer & Interactive 3D South Pole Landing
* **Dual Pre-Launch Gate**: A final flight-readiness review enforces a hard lock on budget overruns while flagging mass overruns as high-risk launch warnings.
* **Telemetry Slow-Motion Cutscene**: A full-screen visualization tracks *Liftoff → Trans-Lunar Injection → Lunar Orbit Insertion*, accompanied by a real-time typewriter telemetry log reporting power and thermal status.
* **3D Lunar South Pole Site Selection & Landing**: Players rotate and zoom a 3D lunar globe to pick a landing site—**Shackleton Crater, Nobile Rim, Cabeus Crater, or Malapert Massif**—and choose a descent profile (Fuel-Saver / Standard / Safety-First), culminating in a 3D PBR landing simulation showing either a nominal touchdown or slope-induced damage[cite: 2].

### 🔹 Act 4: Spectral Data Verification & Engineering Debrief
* **Solving the "False-Positive Trap"**: Players inspect downlinked spectral and neutron count plots to distinguish **true subsurface water ice** from **surface hydroxyl ($\text{OH}$) interference**.
* **Multi-Dimensional Scorecard & Zero-Penalty Iteration**: Generates a 5-axis capability radar chart with transparent physical failure/success attribution, allowing players to **jump directly back to any assembly step** to refine their design and relaunch.

---

## 🤝 4. Single-Player & 4-Player Co-op Mode

Aligned with the challenge's collaborative design goals, the game supports both **solo play** and **up to 4-player team coordination** across specialized engineering roles:
1. **Mission Planner**: Manages overall mission budget, science priorities, and final launch authorization.
2. **Spacecraft & Power Engineer**: Optimizes bus, structure, solar arrays, and batteries for mass and power equilibrium.
3. **Comms & Orbit Specialist**: Configures orbital trajectories, antenna gain, and South Pole landing site selection.
4. **Payload & Science Lead**: Selects scientific instruments and leads final spectral signature verification.

---

## 🎨 5. UI/UX Design Philosophy

* **Aerospace Minimalism**: Maintains **45%–55% clean negative space** to prevent cognitive overload and evoke an authentic mission control console.
* **Tabular Monospace Telemetry**: All dynamic budget, mass, and power readouts use monospace tabular numerals (`JetBrains Mono`) to eliminate layout jitter during live updates.
* **Accessible Microcopy**: Technical aerospace terms (e.g., *PSR — Permanently Shadowed Region*, *TLI — Trans-Lunar Injection*) include concise `≤8-word` plain-language tooltips on first appearance so students and non-specialists can play effortlessly.

---

## 🛰️ 6. NASA Data References & Physics Mapping

All launch vehicle capacities, subsystem power-to-mass ratios, and Lunar South Pole illumination/terrain parameters are calibrated against official NASA mission datasets[cite: 2]:

* **Launch Vehicle Performance**: Derived from *NASA Space Launch System (SLS) Fact Sheets* and *NASA Launch Services Program (LSP)* public Trans-Lunar Injection (TLI) payload benchmarks.
* **Lunar South Pole Topography & Illumination**: Informed by *Lunar Reconnaissance Orbiter (LRO)* **LOLA (Lunar Orbiter Laser Altimeter)** elevation maps and **Diviner Lunar Radiometer Experiment** Permanently Shadowed Region (PSR) thermal data.
* **Water-Ice & Hydroxyl Spectral Models**: Grounded in *LCROSS (Lunar Crater Observation and Sensing Satellite)* impact plume findings, *LRO LEND (Lunar Exploration Neutron Detector)* hydrogen abundance maps, and *NASA VIPER* rover instrument specifications.

---

## 🛠️ 7. Tech Stack & Project Structure

* **Frontend**: React, TypeScript, Vite
* **Styling & Motion**: Tailwind CSS, Framer Motion (`< 200ms` tactile feedback & HUD telemetry transitions)
* **3D Rendering & Data Visualization**: Three.js (3D Lunar South Pole site selection & descent physics) / Custom SVG & Canvas (dynamic CAD spacecraft blueprint & spectral plots)

```text
space-mission-design-game/
├── public/
│   └── assets/                # 2D vector planets, 3D lunar textures, and audio cues
├── src/
│   ├── components/
│   │   ├── act0-briefing/     # Act 0: Home HUD & 3-card micro-tutorial modal
│   │   ├── act1-launcher/     # Act 1: Launch vehicle Coverflow selector
│   │   ├── act2-assembly/     # Act 2: 6-step subsystem workbench & live CAD blueprint
│   │   ├── act3-flight/       # Act 3: Dual launch gate, transfer cutscene & 3D landing
│   │   └── act4-debrief/      # Act 4: Spectral verifier, radar scorecard & debrief
│   ├── data/
│   │   └── missionDatabase.ts # Rockets, subsystems, landing sites & NASA citations
│   ├── engine/
│   │   └── physicsValidator.ts # Resource coupling & failure root-cause engine
│   └── styles/
│       └── tokens.css         # Aerospace Minimalism dark-space & monospace tokens
└── README.md
