"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialHeatmapDataColor``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class GeospatialHeatmapDataColor(TypedDict):
    color: "aws_sdk_quicksight.types.hex_color.HexColor"
    """<p>The hex color to be used in the heatmap point style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialHeatmapDataColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> GeospatialHeatmapDataColor:
    out: GeospatialHeatmapDataColor = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("GeospatialHeatmapDataColor.color required")
    return out
