"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultGridLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.grid_layout_canvas_size_options


class DefaultGridLayoutConfiguration(TypedDict):
    canvas_size_options: "aws_sdk_quicksight.types.grid_layout_canvas_size_options.GridLayoutCanvasSizeOptions"
    """<p>Determines the screen canvas size options for a grid layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultGridLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.grid_layout_canvas_size_options

    out["CanvasSizeOptions"] = (
        aws_sdk_quicksight.types.grid_layout_canvas_size_options.serialize_json(
            value["canvas_size_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> DefaultGridLayoutConfiguration:
    out: DefaultGridLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.grid_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.grid_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    else:
        raise DeserializationError(
            "DefaultGridLayoutConfiguration.canvas_size_options required"
        )
    return out
