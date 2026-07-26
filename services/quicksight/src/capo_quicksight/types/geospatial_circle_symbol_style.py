"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCircleSymbolStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_circle_radius
    import capo_quicksight.types.geospatial_color
    import capo_quicksight.types.geospatial_line_width


class GeospatialCircleSymbolStyle(TypedDict, closed=True):
    fill_color: NotRequired["capo_quicksight.types.geospatial_color.GeospatialColor"]
    """<p>The color and opacity values for the fill color.</p>"""
    stroke_color: NotRequired["capo_quicksight.types.geospatial_color.GeospatialColor"]
    """<p>The color and opacity values for the stroke color.</p>"""
    stroke_width: NotRequired[
        "capo_quicksight.types.geospatial_line_width.GeospatialLineWidth"
    ]
    """<p>The width of the stroke (border).</p>"""
    circle_radius: NotRequired[
        "capo_quicksight.types.geospatial_circle_radius.GeospatialCircleRadius"
    ]
    """<p>The radius of the circle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCircleSymbolStyle) -> dict:
    out: dict = {}
    if "fill_color" in value:
        import capo_quicksight.types.geospatial_color

        out["FillColor"] = capo_quicksight.types.geospatial_color.serialize_json(
            value["fill_color"]
        )
    if "stroke_color" in value:
        import capo_quicksight.types.geospatial_color

        out["StrokeColor"] = capo_quicksight.types.geospatial_color.serialize_json(
            value["stroke_color"]
        )
    if "stroke_width" in value:
        import capo_quicksight.types.geospatial_line_width

        out["StrokeWidth"] = capo_quicksight.types.geospatial_line_width.serialize_json(
            value["stroke_width"]
        )
    if "circle_radius" in value:
        import capo_quicksight.types.geospatial_circle_radius

        out["CircleRadius"] = (
            capo_quicksight.types.geospatial_circle_radius.serialize_json(
                value["circle_radius"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialCircleSymbolStyle:
    out: GeospatialCircleSymbolStyle = {}  # type: ignore[typeddict-item]
    if "FillColor" in data:
        import capo_quicksight.types.geospatial_color

        out["fill_color"] = capo_quicksight.types.geospatial_color.deserialize_json(
            data["FillColor"]
        )
    if "StrokeColor" in data:
        import capo_quicksight.types.geospatial_color

        out["stroke_color"] = capo_quicksight.types.geospatial_color.deserialize_json(
            data["StrokeColor"]
        )
    if "StrokeWidth" in data:
        import capo_quicksight.types.geospatial_line_width

        out["stroke_width"] = (
            capo_quicksight.types.geospatial_line_width.deserialize_json(
                data["StrokeWidth"]
            )
        )
    if "CircleRadius" in data:
        import capo_quicksight.types.geospatial_circle_radius

        out["circle_radius"] = (
            capo_quicksight.types.geospatial_circle_radius.deserialize_json(
                data["CircleRadius"]
            )
        )
    return out
