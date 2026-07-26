"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutCanvasSizeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.grid_layout_screen_canvas_size_options


class GridLayoutCanvasSizeOptions(TypedDict, closed=True):
    screen_canvas_size_options: NotRequired[
        "capo_quicksight.types.grid_layout_screen_canvas_size_options.GridLayoutScreenCanvasSizeOptions"
    ]
    """<p>The options that determine the sizing of the canvas used in a grid layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutCanvasSizeOptions) -> dict:
    out: dict = {}
    if "screen_canvas_size_options" in value:
        import capo_quicksight.types.grid_layout_screen_canvas_size_options

        out["ScreenCanvasSizeOptions"] = (
            capo_quicksight.types.grid_layout_screen_canvas_size_options.serialize_json(
                value["screen_canvas_size_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> GridLayoutCanvasSizeOptions:
    out: GridLayoutCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "ScreenCanvasSizeOptions" in data:
        import capo_quicksight.types.grid_layout_screen_canvas_size_options

        out["screen_canvas_size_options"] = (
            capo_quicksight.types.grid_layout_screen_canvas_size_options.deserialize_json(
                data["ScreenCanvasSizeOptions"]
            )
        )
    return out
