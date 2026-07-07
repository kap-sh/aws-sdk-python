"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.bounding_box


class WaypointOptimizationAvoidanceAreaGeometry(TypedDict, closed=True):
    bounding_box: NotRequired["aws_sdk_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAvoidanceAreaGeometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_geo_routes.types.bounding_box

        out["BoundingBox"] = aws_sdk_geo_routes.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAvoidanceAreaGeometry:
    out: WaypointOptimizationAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_geo_routes.types.bounding_box

        out["bounding_box"] = aws_sdk_geo_routes.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    return out
