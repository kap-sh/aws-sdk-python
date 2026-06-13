"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutScreenCanvasSizeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.resize_option


class GridLayoutScreenCanvasSizeOptions(TypedDict):
    resize_option: "aws_sdk_quicksight.types.resize_option.ResizeOption"
    """<p>This value determines the layout behavior when the viewport is resized.</p> <ul> <li> <p> <code>FIXED</code>: A fixed width will be used when optimizing the layout. In the Quick Sight console, this option is called <code>Classic</code>.</p> </li> <li> <p> <code>RESPONSIVE</code>: The width of the canvas will be responsive and optimized to the view port. In the Quick Sight console, this option is called <code>Tiled</code>.</p> </li> </ul>"""
    optimized_view_port_width: NotRequired[
        "aws_sdk_quicksight.types.pixel_length.PixelLength"
    ]
    """<p>The width that the view port will be optimized for when the layout renders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutScreenCanvasSizeOptions) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.resize_option

    out["ResizeOption"] = aws_sdk_quicksight.types.resize_option.serialize_json(
        value["resize_option"]
    )
    if "optimized_view_port_width" in value:
        out["OptimizedViewPortWidth"] = value["optimized_view_port_width"]
    return out


def deserialize_json(data: dict) -> GridLayoutScreenCanvasSizeOptions:
    out: GridLayoutScreenCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "ResizeOption" in data:
        import aws_sdk_quicksight.types.resize_option

        out["resize_option"] = aws_sdk_quicksight.types.resize_option.deserialize_json(
            data["ResizeOption"]
        )
    else:
        raise DeserializationError(
            "GridLayoutScreenCanvasSizeOptions.resize_option required"
        )
    if "OptimizedViewPortWidth" in data:
        out["optimized_view_port_width"] = data["OptimizedViewPortWidth"]
    return out
