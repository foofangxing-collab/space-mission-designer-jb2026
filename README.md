# 🚀 Space Mission Design Game: Lunar South Pole Water-Ice Explorer
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

## 🎮 3. Gameplay Loop: 5-Act
