"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutCanvasSizeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options


class FreeFormLayoutCanvasSizeOptions(TypedDict):
    screen_canvas_size_options: NotRequired[
        "aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options.FreeFormLayoutScreenCanvasSizeOptions"
    ]
    """<p>The options that determine the sizing of the canvas used in a free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutCanvasSizeOptions) -> dict:
    out: dict = {}
    if "screen_canvas_size_options" in value:
        import aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options

        out["ScreenCanvasSizeOptions"] = (
            aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options.serialize_json(
                value["screen_canvas_size_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> FreeFormLayoutCanvasSizeOptions:
    out: FreeFormLayoutCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "ScreenCanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options

        out["screen_canvas_size_options"] = (
            aws_sdk_quicksight.types.free_form_layout_screen_canvas_size_options.deserialize_json(
                data["ScreenCanvasSizeOptions"]
            )
        )
    return out
