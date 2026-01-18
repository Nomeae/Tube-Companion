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
from textual.containers import Horizontal, Vertical, Center
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
from linestatuses import valid_lines
valid_lines = [valid_lines.title().replace("-", " & ") for valid_lines in valid_lines]
valid_lines.sort()
from stationlookup import stationArrivals
lines = [
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

class TubeCompanion(App):
    CSS_PATH = "markdownconf.tcss"


    def compose(self) -> ComposeResult:
        self.theme = "tokyo-night"
        yield Header()
        with Horizontal(id="buttons"):
            yield Button("Line Statuses", id="linestuff_select")
            yield Button("Station Arrivals", id="stationstuff_select")
        with ContentSwitcher(initial="linestuff"):
            yield DataTable(id="linestuff", cursor_type='none')
            with Center(id="stationstuff_container"):
                with Vertical(id="arrival_container"):
                    yield DataTable(id="arrivaltable", cursor_type='none')
                with Horizontal(id="station_inputs"):
                    yield Input(placeholder="Station Name",
                                tooltip="Find arrivals/departures of Tube stations.",
                                id="stationsearch",
                                type="text"
                                )
                    yield Select.from_values(valid_lines, id="linesearch", type_to_search = True)
                    yield Button("Search", id="submitsearch")
        yield Footer()


    def on_mount(self) -> None:
        table = self.query_one("#linestuff", DataTable)
        table.add_columns(*lines[0])
        table.add_rows(lines[1:])

        table = self.query_one("#arrivaltable", DataTable)
        table.add_columns("Platform", "Towards", "Time (minutes)")

    def table_update(self, station, line) -> None:
        arrivals = stationArrivals(station, line)
        table = self.query_one("#arrivaltable", DataTable)
        table.clear()
        if not table.columns:
            table.add_columns("Platform", "Towards", "Time (minutes)")
        if arrivals:
            for a in arrivals:
                table.add_row(
                    str(a["platform"]),
                    f"[underline]{a['destination']}[/underline]",
                    str(a["time_minutes"])
                )
        else:
            table.add_row("No arrivals", "-", "-")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "linestuff_select":
            self.query_one(ContentSwitcher).current = "linestuff"
        elif event.button.id == "stationstuff_select":
            self.query_one(ContentSwitcher).current = "stationstuff_container"
        elif event.button.id == "submitsearch":
            station = self.query_one("#stationsearch", Input).value
            line = self.query_one("#linesearch", Select).value
            self.table_update(station, line)
            self.set_timer(60, lambda: self.table_update(station, line))

if __name__ == "__main__":
    app = TubeCompanion()
    app.run()