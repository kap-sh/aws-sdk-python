"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLineSymbolStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_color
    import capo_quicksight.types.geospatial_line_width


class GeospatialLineSymbolStyle(TypedDict, closed=True):
    fill_color: NotRequired["capo_quicksight.types.geospatial_color.GeospatialColor"]
    """<p>The color and opacity values for the fill color.</p>"""
    line_width: NotRequired[
        "capo_quicksight.types.geospatial_line_width.GeospatialLineWidth"
    ]
    """<p>The width value for a line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLineSymbolStyle) -> dict:
    out: dict = {}
    if "fill_color" in value:
        import capo_quicksight.types.geospatial_color

        out["FillColor"] = capo_quicksight.types.geospatial_color.serialize_json(
            value["fill_color"]
        )
    if "line_width" in value:
        import capo_quicksight.types.geospatial_line_width

        out["LineWidth"] = capo_quicksight.types.geospatial_line_width.serialize_json(
            value["line_width"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialLineSymbolStyle:
    out: GeospatialLineSymbolStyle = {}  # type: ignore[typeddict-item]
    if "FillColor" in data:
        import capo_quicksight.types.geospatial_color

        out["fill_color"] = capo_quicksight.types.geospatial_color.deserialize_json(
            data["FillColor"]
        )
    if "LineWidth" in data:
        import capo_quicksight.types.geospatial_line_width

        out["line_width"] = (
            capo_quicksight.types.geospatial_line_width.deserialize_json(
                data["LineWidth"]
            )
        )
    return out
