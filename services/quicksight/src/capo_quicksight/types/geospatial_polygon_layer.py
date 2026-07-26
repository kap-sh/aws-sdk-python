"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPolygonLayer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_polygon_style


class GeospatialPolygonLayer(TypedDict, closed=True):
    style: "capo_quicksight.types.geospatial_polygon_style.GeospatialPolygonStyle"
    """<p>The visualization style for a polygon layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPolygonLayer) -> dict:
    out: dict = {}
    import capo_quicksight.types.geospatial_polygon_style

    out["Style"] = capo_quicksight.types.geospatial_polygon_style.serialize_json(
        value["style"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialPolygonLayer:
    out: GeospatialPolygonLayer = {}  # type: ignore[typeddict-item]
    if "Style" in data:
        import capo_quicksight.types.geospatial_polygon_style

        out["style"] = capo_quicksight.types.geospatial_polygon_style.deserialize_json(
            data["Style"]
        )
    else:
        raise DeserializationError("GeospatialPolygonLayer.style required")
    return out
