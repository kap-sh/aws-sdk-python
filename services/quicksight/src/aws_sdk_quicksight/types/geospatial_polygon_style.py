"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPolygonStyle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_polygon_symbol_style


class GeospatialPolygonStyle(TypedDict):
    polygon_symbol_style: NotRequired[
        "aws_sdk_quicksight.types.geospatial_polygon_symbol_style.GeospatialPolygonSymbolStyle"
    ]
    """<p>The polygon symbol style for a polygon layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPolygonStyle) -> dict:
    out: dict = {}
    if "polygon_symbol_style" in value:
        import aws_sdk_quicksight.types.geospatial_polygon_symbol_style

        out["PolygonSymbolStyle"] = (
            aws_sdk_quicksight.types.geospatial_polygon_symbol_style.serialize_json(
                value["polygon_symbol_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialPolygonStyle:
    out: GeospatialPolygonStyle = {}  # type: ignore[typeddict-item]
    if "PolygonSymbolStyle" in data:
        import aws_sdk_quicksight.types.geospatial_polygon_symbol_style

        out["polygon_symbol_style"] = (
            aws_sdk_quicksight.types.geospatial_polygon_symbol_style.deserialize_json(
                data["PolygonSymbolStyle"]
            )
        )
    return out
