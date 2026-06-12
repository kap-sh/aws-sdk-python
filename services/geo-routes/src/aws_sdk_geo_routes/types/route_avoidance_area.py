"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceArea``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry_list

RouteAvoidanceArea = TypedDict(
    "RouteAvoidanceArea",
    {
        "except": NotRequired[
            "aws_sdk_geo_routes.types.route_avoidance_area_geometry_list.RouteAvoidanceAreaGeometryList"
        ],
        "geometry": "aws_sdk_geo_routes.types.route_avoidance_area_geometry.RouteAvoidanceAreaGeometry",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceArea) -> dict:
    out: dict = {}
    if "except" in value:
        import aws_sdk_geo_routes.types.route_avoidance_area_geometry_list

        out["Except"] = (
            aws_sdk_geo_routes.types.route_avoidance_area_geometry_list.serialize_json(
                value["except"]
            )
        )
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry

    out["Geometry"] = (
        aws_sdk_geo_routes.types.route_avoidance_area_geometry.serialize_json(
            value["geometry"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteAvoidanceArea:
    out: RouteAvoidanceArea = {}  # type: ignore[typeddict-item]
    if "Except" in data:
        import aws_sdk_geo_routes.types.route_avoidance_area_geometry_list

        out["except"] = (
            aws_sdk_geo_routes.types.route_avoidance_area_geometry_list.deserialize_json(
                data["Except"]
            )
        )
    if "Geometry" in data:
        import aws_sdk_geo_routes.types.route_avoidance_area_geometry

        out["geometry"] = (
            aws_sdk_geo_routes.types.route_avoidance_area_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError("RouteAvoidanceArea.geometry required")
    return out
