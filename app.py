import os
import json
import numpy as np
import pandas as pd
import panel as pn
import pyvista as pv
from pyvista import Plotter

pn.extension("vtk")

DATA_DIR = "./data"


def load_json_files():
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    return {f: os.path.join(DATA_DIR, f) for f in files}


def load_json_to_df(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return pd.json_normalize(data)


# Widgets
file_selector = pn.widgets.Select(name="Select JSON File", options=load_json_files())
plot_type = pn.widgets.Select(
    name="Plot Type", options=["scatter", "line"]
)  # Add more types here

x_axis = pn.widgets.Select(name="X Axis")
y_axis = pn.widgets.Select(name="Y Axis")


# Create an empty placeholder with a dummy VTK object
dummy_plotter = pv.Plotter(off_screen=True)
dummy_plotter.add_text("Select data to plot", font_size=12)
vtk_pane = pn.pane.VTK(dummy_plotter.ren_win, sizing_mode="stretch_both", height=400)


def update_fields(event=None):
    path = file_selector.value
    if path:
        df = load_json_to_df(path)
        columns = list(df.columns)
        x_axis.options = columns
        y_axis.options = columns


file_selector.param.watch(update_fields, "value")


def update_plot(event=None):
    if not (x_axis.value and y_axis.value):
        return

    df = load_json_to_df(file_selector.value)
    x = df[x_axis.value].values
    y = df[y_axis.value].values

    plotter = Plotter(off_screen=True)
    if plot_type.value == "scatter":
        plotter.add_points(
            pv.PolyData(np.column_stack((x, y, y * 0))), render_points_as_spheres=True
        )
    elif plot_type.value == "line":
        points = np.column_stack((x, y, y * 0))
        lines = np.arange(0, len(points), dtype=np.int32)
        cells = np.insert(lines, 0, len(lines))
        pdata = pv.PolyData()
        pdata.points = points
        pdata.lines = cells
        plotter.add_mesh(pdata, line_width=2)

    vtk_pane.object = plotter.ren_win


for w in [plot_type, x_axis, y_axis]:
    w.param.watch(update_plot, "value")

layout = pn.Column(
    "# PanelVista", pn.Row(file_selector, plot_type), pn.Row(x_axis, y_axis), vtk_pane
)

update_fields()

layout.servable()
