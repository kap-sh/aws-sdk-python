"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialNullSymbolStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_width
    import aws_sdk_quicksight.types.hex_color_with_transparency


class GeospatialNullSymbolStyle(TypedDict, closed=True):
    fill_color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The color and opacity values for the fill color.</p>"""
    stroke_color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The color and opacity values for the stroke color.</p>"""
    stroke_width: NotRequired[
        "aws_sdk_quicksight.types.geospatial_width.GeospatialWidth"
    ]
    """<p>The width of the border stroke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialNullSymbolStyle) -> dict:
    out: dict = {}
    if "fill_color" in value:
        out["FillColor"] = value["fill_color"]
    if "stroke_color" in value:
        out["StrokeColor"] = value["stroke_color"]
    if "stroke_width" in value:
        out["StrokeWidth"] = value["stroke_width"]
    return out


def deserialize_json(data: dict) -> GeospatialNullSymbolStyle:
    out: GeospatialNullSymbolStyle = {}  # type: ignore[typeddict-item]
    if "FillColor" in data:
        out["fill_color"] = data["FillColor"]
    if "StrokeColor" in data:
        out["stroke_color"] = data["StrokeColor"]
    if "StrokeWidth" in data:
        out["stroke_width"] = data["StrokeWidth"]
    return out
