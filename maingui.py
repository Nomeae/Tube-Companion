from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    DataTable,
    ContentSwitcher,
    Button,
    Label,
)

from textual.containers import Horizontal, Vertical

from linestatuses import (
    bakerloo,
    central,
    circle,
    district,
    hammersmith,
    jubilee,
    metropolitan,
    northern,
    piccadilly,
    victoria,
    waterloo
)

from linestatuses import valid_lines, stationget

valid_lines = [valid_lines.title().replace("-", " & ") for valid_lines in valid_lines]
valid_lines.sort()

ROWS = [
    ("Line", "Status"),
    ("Bakerloo", bakerloo()),
    ("Central", central()),
    ("Circle", circle()),
    ("District", district()),
    ("Hammersmith & City", hammersmith()),
    ("Jubilee", jubilee()),
    ("Metropolitan", metropolitan()),
    ("Northern", northern()),
    ("Piccadilly", piccadilly()),
    ("Victoria", victoria()),
    ("Waterloo & City", waterloo()),
]

#THEMES/COLOURS
good = "#72e090"
okay = "#ffa742"
bad = "#f75a52"

class TubeCompanion(App):
    CSS_PATH = "markdownconf.tcss"
    ENABLE_COMMAND_PALETTE = False

#everything below is app stuff

    def compose(self) -> ComposeResult:
        self.theme = "tokyo-night"
        yield Header()

        with Horizontal(id="buttons"):
            yield Button("Line Statuses", id="linestuff")
            yield Button("Station Info", id="stationstuff")

        with ContentSwitcher(initial="linestuff"):
            yield DataTable(id="linestuff", cursor_type='none')

            with Vertical(id="stationstuff"):

                yield Label("This feature is a work in progress at the moment sorry... "
                            "Coming in an update soon!", id="wip")

        yield Footer()

    def on_mount(self) -> None:
        self.title = "Tube Companion"
        self.sub_title = "0.1"
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id

if __name__ == "__main__":
    app = TubeCompanion()
    app.run()