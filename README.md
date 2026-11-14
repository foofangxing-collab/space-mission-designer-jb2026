# 🚀 Space Mission Design Game:
**2026 NASA Space Apps Challenge — Space Mission Design Game**

> Space Mission Design Game is an interactive space mission design game where players take on the role of a mission designer and plan a spacecraft mission to explore the Moon's South Pole.

Players make engineering decisions, manage limited resources, select mission equipment, and experience how their choices can influence mission success — while discovering the science behind lunar water ice.

[🌐 Live Demo](#) · [🎬 30s Demo Video](#) · [📚 NASA Data References](#-6-nasa-data-references--physics-mapping)

---

## 📖 1. Project Vision & Core Problem

In traditional space science education, learners often encounter isolated concepts—such as a single orbital equation or rocket thrust formula—without experiencing how **science objectives, engineering constraints, resource budgets, and mission operations** interlock in a real spaceflight program.

**Space Mission Design Game** bridges this gap. Centered on a cutting-edge mission scenario—**"Hunting Lunar Water Ice: South Pole Exploration"**—This is the example mission inside provided in this game. Players take on the role of Chief Mission Designer to balance competing constraints within a finite resource pool. **There is no single "correct" solution:** whether you pair a cost-effective commercial launcher with a lightweight payload or deploy a heavy-lift rocket carrying high-precision spectrometers, any architecture that survives physics validation and resource limits can reach the lunar south pole.

---
## 🎯 2. Project Objectives

1. Introduce beginners to the fundamentals of space mission design.
2. Demonstrate the relationship between spacecraft components and mission resources.
3. Encourage engineering decision-making through interactive challenges.
4. Introduce the scientific importance each mission designed.
5. Make space exploration more accessible and engaging through gameplay.
   
---
## 📌 3. Key Features

- **Interactive Mission Design**: Select mission equipment and configure a spacecraft.
- **Spacecraft Customisation**: Explore different spacecraft platforms and subsystems.
- **Resource Management**: Balance mission budget, spacecraft mass, power, and other constraints.
- **Mission Planning**: Make decisions about launch vehicles, orbits, landing locations, and mission operations.
- **3D Visualisation**: Explore spacecraft and lunar environments through interactive 3D elements.
- **Science Exploration**: Learn about our space and the scientific purpose of exploring the space.
- **Mission Evaluation**: Review mission performance and understand how design decisions influence the outcome.
- **Science Snippets**: Short and interesting science facts appear throughout the gameplay to make learning about lunar exploration more engaging.

---
## ⚖️ 3. Core Engineering Trade-offs

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

## 🎮 4. How to Play

The game guides players through the major 6 stages of a lunar exploration mission. 

### 🔹 Stage 1 — Mission Briefing
* Understand the mission objectives, the lunar South Pole environment, and the importance of investigating water ice.

### 🔹 Stage 2 — Launch Vehicle Selection
* Compare available launch vehicles and consider their payload capabilities and mission costs..

### 🔹 Stage 3 — Spacecraft Design
* Designed around **Hick's Law**, players assemble their spacecraft sequentially by selecting six subsystems[cite: 2]. Each step displays only 3–4 high-contrast component cards while dynamically illuminating a live CAD blueprint and telemetry bars (`< 200ms` response):
  1. `Platform` (Spacecraft Bus)
  2. `Structure` (Primary Load-Bearing & Thermal Structure)
  3. `Solar Panel` (Photovoltaic Arrays)
  4. `Battery` (Deep-Space Energy Storage)
  5. `Antenna` (High-Gain Communications)
  6. `Scientific Instrument` (Neutron Spectrometer, Near-Infrared Spectrometer, etc.)

Each selection contributes to the spacecraft's overall design and resource requirements.

### 🔹 Stage 4 — Mission Planning
* Choose an appropriate orbit and allocate resources before the mission begins. Review the spacecraft configuration and identify potential design constraints.

### 🔹 Stage 5 - Launch, Transfer & Interactive 3D South Pole Landing
Experience the mission's journey from launch to the Moon.

* **Dual Pre-Launch Gate**: A final flight-readiness review enforces a hard lock on budget overruns while flagging mass overruns as high-risk launch warnings.
* **Telemetry Slow-Motion Cutscene**: A full-screen visualization tracks *Liftoff → Trans-Lunar Injection → Lunar Orbit Insertion*, accompanied by a real-time typewriter telemetry log reporting power and thermal status.
* **3D Lunar South Pole Site Selection & Landing**: Players rotate and zoom a 3D lunar globe to pick a landing site—**Shackleton Crater, Nobile Rim, Cabeus Crater, or Malapert Massif**—and choose a descent profile (Fuel-Saver / Standard / Safety-First), culminating in a 3D PBR landing simulation showing either a nominal touchdown or slope-induced damage

### 🔹 Stage 6 — Lunar Exploration and Mission Results
Explore the lunar environment, investigate the mission's scientific objectives, and review the final mission performance.

* **Multi-Dimensional Scorecard & Zero-Penalty Iteration**: Generates a 5-axis capability radar chart with transparent physical failure/success attribution, allowing players to **jump directly back to any assembly step** to refine their design and relaunch.

---

## 🎨 5. UI/UX Design Philosophy

* **Aerospace Minimalism**: Maintains **45%–55% clean negative space** to prevent cognitive overload and evoke an authentic mission control console.
* **Tabular Monospace Telemetry**: All dynamic budget, mass, and power readouts use monospace tabular numerals (`JetBrains Mono`) to eliminate layout jitter during live updates.
* **Accessible Microcopy**: Technical aerospace terms (e.g., *PSR — Permanently Shadowed Region*, *TLI — Trans-Lunar Injection*) include concise `≤8-word` plain-language tooltips on first appearance so students and non-specialists can play effortlessly.

---

## 🛰️ 6. NASA Data References & Physics Mapping

All launch vehicle capacities, subsystem power-to-mass ratios, and Lunar South Pole illumination/terrain parameters are calibrated against official NASA mission datasets:

* **Launch Vehicle Performance**: Derived from *NASA Space Launch System (SLS) Fact Sheets* and *NASA Launch Services Program (LSP)* public Trans-Lunar Injection (TLI) payload benchmarks.
* **Lunar South Pole Topography & Illumination**: Informed by *Lunar Reconnaissance Orbiter (LRO)* **LOLA (Lunar Orbiter Laser Altimeter)** elevation maps and **Diviner Lunar Radiometer Experiment** Permanently Shadowed Region (PSR) thermal data.
* **Water-Ice & Hydroxyl Spectral Models**: Grounded in *LCROSS (Lunar Crater Observation and Sensing Satellite)* impact plume findings, *LRO LEND (Lunar Exploration Neutron Detector)* hydrogen abundance maps, and *NASA VIPER* rover instrument specifications.

---

## 🛠️ 7. Tech Stack & Project Structure

* **HTML**: To structure the web application.
* **CSS**: To customize the interface, layout, animations, and visual appearance.
* **JavaScript**: To implement game logic, user interactions, and mission simulations.
* **React 18**: To build interactive user interface components and manage application states.
* **Tailwind CSS**: To create responsive layouts and style interface elements.
* **Three.js**: To create interactive 3D visualizations of rockets, spacecraft, and lunar environments.
* **Babel Standalone**: To compile JSX directly in the browser.
* **Visual Studio Code**: For writing and editing the source code.
* **Git and GitHub**: For version control and source code management

