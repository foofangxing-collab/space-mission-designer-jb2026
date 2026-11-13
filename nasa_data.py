MISSIONS = {
    "moon_south_pole": {
        "name": "Lunar South Pole Water Ice Hunt (Artemis / VIPER)",
        "budget_limit": 500,
        "distance_zone": "near",
        "hazard": "extreme_cold",
        "description": "Explore permanently shadowed craters at the Lunar South Pole to locate water ice deposits.",
        "nasa_reference": "https://www.nasa.gov/mission/viper/"
    },
    "mars_sample_search": {
        "name": "Mars Biosignature & Sample Mission (Perseverance)",
        "budget_limit": 1800,
        "distance_zone": "mars",
        "hazard": "dust_storms",
        "description": "Land on Jezero Crater to search for signs of ancient microbial life and cache rock samples.",
        "nasa_reference": "https://mars.nasa.gov/mars2020/"
    },
    "europa_ocean_probe": {
        "name": "Europa Ice-Shell & Ocean Recon (Europa Clipper)",
        "budget_limit": 3500,
        "distance_zone": "deep_space",
        "hazard": "intense_radiation",
        "description": "Conduct detailed reconnaissance of Jupiter's icy moon Europa to investigate its subsurface ocean.",
        "nasa_reference": "https://europa.nasa.gov/"
    }
}

PARTS = {
    "rockets": [
        {
            "id": "electron",
            "name": "Rocket Lab Electron (Small-Lift)",
            "cost": 15,
            "max_payload": 300,
            "weight": 0,
            "power_supply": 0,
            "power_draw": 0,
            "science_score": 0,
            "info": "Agile small-lift rocket ideal for lightweight lunar micro-rovers and tight budgets."
        },
        {
            "id": "falcon_9",
            "name": "SpaceX Falcon 9 (Medium-Lift)",
            "cost": 70,
            "max_payload": 2500,
            "weight": 0,
            "power_supply": 0,
            "power_draw": 0,
            "science_score": 0,
            "info": "Workhorse reusable medium-lift rocket balancing cost and payload capacity."
        },
        {
            "id": "falcon_heavy",
            "name": "SpaceX Falcon Heavy (Heavy-Lift)",
            "cost": 150,
            "max_payload": 6000,
            "weight": 0,
            "power_supply": 0,
            "power_draw": 0,
            "science_score": 0,
            "info": "Triple-core heavy rocket capable of sending large science payloads to Mars and Jupiter."
        },
        {
            "id": "sls_block1",
            "name": "NASA Space Launch System (SLS Super Heavy)",
            "cost": 900,
            "max_payload": 15000,
            "weight": 0,
            "power_supply": 0,
            "power_draw": 0,
            "science_score": 0,
            "info": "NASA's flagship super heavy-lift launch vehicle built for deep space exploration."
        }
    ],
    "power": [
        {
            "id": "compact_solar",
            "name": "Compact GaAs Solar Array",
            "cost": 40,
            "max_payload": 0,
            "weight": 60,
            "power_supply": 350,
            "power_draw": 0,
            "science_score": 10,
            "info": "Lightweight gallium-arsenide solar panels. Great near Earth/Moon, weak in deep space."
        },
        {
            "id": "mega_solar_wings",
            "name": "Deployable Mega Solar Wings (Clipper-Class)",
            "cost": 180,
            "max_payload": 0,
            "weight": 420,
            "power_supply": 1100,
            "power_draw": 0,
            "science_score": 30,
            "info": "Massive solar arrays spanning over 30 meters to capture faint sunlight in the outer solar system."
        },
        {
            "id": "mmrtg_nuclear",
            "name": "MMRTG Nuclear Battery (Plutonium-238)",
            "cost": 450,
            "max_payload": 0,
            "weight": 120,
            "power_supply": 800,
            "power_draw": 0,
            "science_score": 80,
            "info": "Multi-Mission Radioisotope Thermoelectric Generator. Immune to dust storms, darkness, and distance."
        }
    ],
    "comms_protection": [
        {
            "id": "low_gain_antenna",
            "name": "S-Band Low-Gain Omni Antenna",
            "cost": 25,
            "max_payload": 0,
            "weight": 20,
            "power_supply": 0,
            "power_draw": 50,
            "science_score": 10,
            "info": "Basic omnidirectional antenna suitable for Lunar proximity. Cannot reach Earth from Mars or Jupiter."
        },
        {
            "id": "high_gain_dish",
            "name": "X/Ka-Band Deep Space High-Gain Dish",
            "cost": 160,
            "max_payload": 0,
            "weight": 180,
            "power_supply": 0,
            "power_draw": 220,
            "science_score": 60,
            "info": "High-precision parabolic dish required to beam scientific telemetry back from Mars and deep space."
        },
        {
            "id": "rad_thermal_vault",
            "name": "Titanium Radiation Vault & Cryo-Heaters",
            "cost": 280,
            "max_payload": 0,
            "weight": 550,
            "power_supply": 0,
            "power_draw": 180,
            "science_score": 70,
            "info": "Thick titanium shielding and radioisotope heaters protecting electronics from Jupiter's radiation and lunar cold."
        }
    ],
    "science": [
        {
            "id": "mastcam_z",
            "name": "Mastcam-Z HD Panoramic Stereo Camera",
            "cost": 60,
            "max_payload": 0,
            "weight": 35,
            "power_supply": 0,
            "power_draw": 60,
            "science_score": 120,
            "info": "Zoomable high-definition color cameras to capture geology and landing site panoramas."
        },
        {
            "id": "supercam_laser",
            "name": "SuperCam Laser Micro-Imager & Spectrometer",
            "cost": 140,
            "max_payload": 0,
            "weight": 90,
            "power_supply": 0,
            "power_draw": 140,
            "science_score": 240,
            "info": "Fires a pulsed laser at rocks from meters away to analyze chemical and mineral composition."
        },
        {
            "id": "rimfax_radar",
            "name": "RIMFAX Subsurface Ice-Penetrating Radar",
            "cost": 170,
            "max_payload": 0,
            "weight": 110,
            "power_supply": 0,
            "power_draw": 160,
            "science_score": 280,
            "info": "Uses radar waves to map underground water ice layers and geological strata beneath the surface."
        },
        {
            "id": "sample_drill_arm",
            "name": "Robotic Coring Drill & Sample Caching Arm",
            "cost": 350,
            "max_payload": 0,
            "weight": 480,
            "power_supply": 0,
            "power_draw": 320,
            "science_score": 450,
            "info": "Heavy-duty robotic arm that drills core samples and seals them for potential Earth return."
        },
        {
            "id": "magnetometer_plasma",
            "name": "ICEMAG Magnetometer & Plasma Spectrometer",
            "cost": 190,
            "max_payload": 0,
            "weight": 130,
            "power_supply": 0,
            "power_draw": 150,
            "science_score": 310,
            "info": "Measures magnetic fields and charged particles to confirm the depth and salinity of subsurface oceans."
        },
        {
            "id": "ingenuity_scout",
            "name": "Autonomous Aerial Scout Helicopter (Ingenuity-Class)",
            "cost": 220,
            "max_payload": 0,
            "weight": 85,
            "power_supply": 0,
            "power_draw": 120,
            "science_score": 360,
            "info": "Lightweight autonomous rotorcraft that scouts ahead of rovers to identify high-value science targets."
        }
    ]
}

if __name__ == "__main__":
    total_parts = sum(len(category) for category in PARTS.values())
    print(f"Success: Loaded {len(MISSIONS)} NASA missions and {total_parts} parts!")