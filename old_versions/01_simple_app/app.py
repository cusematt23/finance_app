from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),#inputs go to the server
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*5 is {input.n() * 5}" #"txt" above looks for the txt fn


app = App(app_ui, server)
