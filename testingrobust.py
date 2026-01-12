from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Header,
    DataTable,
    ContentSwitcher,
    Button,
    Input,
    Select,
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

class TubeCompanion(App): #create actual app
    CSS_PATH = "markdownconf.tcss"

#everything below is app stuff

    def compose(self) -> ComposeResult: #widgets within app
        self.theme = "tokyo-night"
        yield Header()


        with Horizontal(id="buttons"):
            yield Button("Line Statuses", id="linestuff")
            yield Button("Station Info", id="stationstuff")

        with ContentSwitcher(initial="linestuff"):
            yield DataTable(id="linestuff", cursor_type='none')
            with Vertical(id="stationstuff"):

                yield Input(placeholder="Station Name",
                            tooltip="Find arrivals/departures of Tube stations.",
                            id="stationsearch",
                            type="text"
                            )

                yield Select.from_values(valid_lines)
                yield Button("Search", id="submitsearch")

        yield Footer()

    def on_select_changed(self, event: Select.Changed) -> None:
        station = event.value
        self.log(f"typed {station}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        line = event.value
        self.log(f"picked {line}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.input.id == "submitsearch":
            stationget()

    def on_mount(self) -> None:  # create table with data in it or something
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id




if __name__ == "__main__":
    app = TubeCompanion()
    app.run()