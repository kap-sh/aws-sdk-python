"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPolygonSymbolStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_color
    import aws_sdk_quicksight.types.geospatial_line_width


class GeospatialPolygonSymbolStyle(TypedDict):
    fill_color: NotRequired["aws_sdk_quicksight.types.geospatial_color.GeospatialColor"]
    """<p>The color and opacity values for the fill color.</p>"""
    stroke_color: NotRequired[
        "aws_sdk_quicksight.types.geospatial_color.GeospatialColor"
    ]
    """<p>The color and opacity values for the stroke color.</p>"""
    stroke_width: NotRequired[
        "aws_sdk_quicksight.types.geospatial_line_width.GeospatialLineWidth"
    ]
    """<p>The width of the border stroke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPolygonSymbolStyle) -> dict:
    out: dict = {}
    if "fill_color" in value:
        import aws_sdk_quicksight.types.geospatial_color

        out["FillColor"] = aws_sdk_quicksight.types.geospatial_color.serialize_json(
            value["fill_color"]
        )
    if "stroke_color" in value:
        import aws_sdk_quicksight.types.geospatial_color

        out["StrokeColor"] = aws_sdk_quicksight.types.geospatial_color.serialize_json(
            value["stroke_color"]
        )
    if "stroke_width" in value:
        import aws_sdk_quicksight.types.geospatial_line_width

        out["StrokeWidth"] = (
            aws_sdk_quicksight.types.geospatial_line_width.serialize_json(
                value["stroke_width"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialPolygonSymbolStyle:
    out: GeospatialPolygonSymbolStyle = {}  # type: ignore[typeddict-item]
    if "FillColor" in data:
        import aws_sdk_quicksight.types.geospatial_color

        out["fill_color"] = aws_sdk_quicksight.types.geospatial_color.deserialize_json(
            data["FillColor"]
        )
    if "StrokeColor" in data:
        import aws_sdk_quicksight.types.geospatial_color

        out["stroke_color"] = (
            aws_sdk_quicksight.types.geospatial_color.deserialize_json(
                data["StrokeColor"]
            )
        )
    if "StrokeWidth" in data:
        import aws_sdk_quicksight.types.geospatial_line_width

        out["stroke_width"] = (
            aws_sdk_quicksight.types.geospatial_line_width.deserialize_json(
                data["StrokeWidth"]
            )
        )
    return out
