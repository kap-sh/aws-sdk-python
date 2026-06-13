"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPolygonLayer``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_polygon_style


class GeospatialPolygonLayer(TypedDict):
    style: "aws_sdk_quicksight.types.geospatial_polygon_style.GeospatialPolygonStyle"
    """<p>The visualization style for a polygon layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPolygonLayer) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.geospatial_polygon_style

    out["Style"] = aws_sdk_quicksight.types.geospatial_polygon_style.serialize_json(
        value["style"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialPolygonLayer:
    out: GeospatialPolygonLayer = {}  # type: ignore[typeddict-item]
    if "Style" in data:
        import aws_sdk_quicksight.types.geospatial_polygon_style

        out["style"] = (
            aws_sdk_quicksight.types.geospatial_polygon_style.deserialize_json(
                data["Style"]
            )
        )
    else:
        raise DeserializationError("GeospatialPolygonLayer.style required")
    return out
