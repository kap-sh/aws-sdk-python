"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutScreenCanvasSizeOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pixel_length


class FreeFormLayoutScreenCanvasSizeOptions(TypedDict):
    optimized_view_port_width: "aws_sdk_quicksight.types.pixel_length.PixelLength"
    """<p>The width that the view port will be optimized for when the layout renders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutScreenCanvasSizeOptions) -> dict:
    out: dict = {}
    out["OptimizedViewPortWidth"] = value["optimized_view_port_width"]
    return out


def deserialize_json(data: dict) -> FreeFormLayoutScreenCanvasSizeOptions:
    out: FreeFormLayoutScreenCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "OptimizedViewPortWidth" in data:
        out["optimized_view_port_width"] = data["OptimizedViewPortWidth"]
    else:
        raise DeserializationError(
            "FreeFormLayoutScreenCanvasSizeOptions.optimized_view_port_width required"
        )
    return out
