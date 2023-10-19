from shiny import App, render, ui, reactive, Session

import numpy as np
import pandas as pd
import yfinance as yf
import plotly.express as px

from pathlib import Path

#DEFAULT APP INPUTS
TITLE="PyShiny Financial Analysis"

#LAYOUT
page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css",href="style.css")
)

app_ui = ui.page_navbar(
    ui.nav(
        "Something cool!", 
        "This is RAD!!!!"),
    ui.nav(
        "Stock Analysis",
        ui.layout_sidebar(
            sidebar=ui.panel_sidebar(
                ui.h2("Hello Shiny!"),
                ui.input_slider("n", "N", 0, 100, 20),
                width=3
            ),
            main=ui.panel_main(
                ui.h2(
                    ui.output_text("txt")
                ),
                ui.navset_pill_card(
                    ui.nav(
                        "Company Summary",
                        "TODO - Summary"
                    ),
                    ui.nav(
                        "Chart",
                        "TODO - Chart"
                    ),
                    ui.nav(
                        "Income Statement",
                        "TODO - Income Statement"
                    )
                )
            )
        )
    ),
    title=ui.tags.div(
        ui.img(src="shipit.png", height="50px", style="margin:5px;"),
        ui.h4(" " + TITLE),
        style="display:flex;-webkit-filter: drop-shadow(2px 2px 2px #222);"
    ),
    bg="#0062cc",
    inverse=True,
    header=page_dependencies       
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"




www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)

