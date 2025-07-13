
# PanelVista

**PanelVista** is a real-time interactive visualization tool using [PyVista](https://github.com/pyvista/pyvista) and [Panel](https://panel.holoviz.org/). It parses local JSON files, lets you select fields and plot types dynamically, and visualizes data live.

## Features

- Parse JSON files from a local folder
- Select plot types (scatter, line, surface, etc.)
- Pick axes and fields dynamically
- Real-time updates as data changes
- Built using Panel (HoloViz) and PyVista for rich, interactive visuals

---

## Tech Stack

* [Panel](https://panel.holoviz.org/)
* [PyVista](https://github.com/pyvista/pyvista)
* [Pandas](https://pandas.pydata.org/) for JSON parsing
* [VTK](https://vtk.org/) under the hood

---


## 📌 Roadmap

* [x] JSON parsing and field selection
* [ ] Live folder watching / auto-refresh
* [ ] Save plot presets
* [ ] Export visuals as PNG/GLTF


## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Install

```bash
# 1. Clone repo
git clone https://github.com/yourname/PanelVista.git
cd PanelVista

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment

# On Mac/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
panel serve app.py --autoreload
```

### Run

```bash
panel serve app.py --autoreload
```

---

## Folder Structure

```
PanelVista/
├── .venv/                 # virtual environment (ignored in git)
├── data/                 # JSON files go here
├── app.py                # main Panel app
├── requirements.txt      # pinned deps
├── requirements-dev.txt  # (optional) dev tools
├── README.md
└── .gitignore
```

---

