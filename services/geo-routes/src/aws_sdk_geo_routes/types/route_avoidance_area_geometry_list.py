"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaGeometryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry

RouteAvoidanceAreaGeometryList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_avoidance_area_geometry.RouteAvoidanceAreaGeometry"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaGeometryList) -> list:
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_avoidance_area_geometry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteAvoidanceAreaGeometryList:
    import aws_sdk_geo_routes.types.route_avoidance_area_geometry

    out: RouteAvoidanceAreaGeometryList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_avoidance_area_geometry.deserialize_json(
                item
            )
        )
    return out
