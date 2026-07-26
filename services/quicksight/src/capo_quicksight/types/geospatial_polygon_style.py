"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPolygonStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_polygon_symbol_style


class GeospatialPolygonStyle(TypedDict, closed=True):
    polygon_symbol_style: NotRequired[
        "capo_quicksight.types.geospatial_polygon_symbol_style.GeospatialPolygonSymbolStyle"
    ]
    """<p>The polygon symbol style for a polygon layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPolygonStyle) -> dict:
    out: dict = {}
    if "polygon_symbol_style" in value:
        import capo_quicksight.types.geospatial_polygon_symbol_style

        out["PolygonSymbolStyle"] = (
            capo_quicksight.types.geospatial_polygon_symbol_style.serialize_json(
                value["polygon_symbol_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialPolygonStyle:
    out: GeospatialPolygonStyle = {}  # type: ignore[typeddict-item]
    if "PolygonSymbolStyle" in data:
        import capo_quicksight.types.geospatial_polygon_symbol_style

        out["polygon_symbol_style"] = (
            capo_quicksight.types.geospatial_polygon_symbol_style.deserialize_json(
                data["PolygonSymbolStyle"]
            )
        )
    return out
