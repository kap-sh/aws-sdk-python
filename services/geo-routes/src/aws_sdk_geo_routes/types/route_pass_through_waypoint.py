"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePassThroughWaypoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pass_through_place


class RoutePassThroughWaypoint(TypedDict, closed=True):
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    place: "aws_sdk_geo_routes.types.route_pass_through_place.RoutePassThroughPlace"
    """<p>Place details corresponding to the pass-through waypoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePassThroughWaypoint) -> dict:
    out: dict = {}
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    import aws_sdk_geo_routes.types.route_pass_through_place

    out["Place"] = aws_sdk_geo_routes.types.route_pass_through_place.serialize_json(
        value["place"]
    )
    return out


def deserialize_json(data: dict) -> RoutePassThroughWaypoint:
    out: RoutePassThroughWaypoint = {}  # type: ignore[typeddict-item]
    if "GeometryOffset" in data:
        out["geometry_offset"] = data["GeometryOffset"]
    if "Place" in data:
        import aws_sdk_geo_routes.types.route_pass_through_place

        out["place"] = (
            aws_sdk_geo_routes.types.route_pass_through_place.deserialize_json(
                data["Place"]
            )
        )
    else:
        raise DeserializationError("RoutePassThroughWaypoint.place required")
    return out
