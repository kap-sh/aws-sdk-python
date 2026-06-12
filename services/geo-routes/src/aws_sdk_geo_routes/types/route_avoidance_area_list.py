"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_avoidance_area

RouteAvoidanceAreaList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_avoidance_area.RouteAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaList) -> list:
    import aws_sdk_geo_routes.types.route_avoidance_area

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_avoidance_area.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteAvoidanceAreaList:
    import aws_sdk_geo_routes.types.route_avoidance_area

    out: RouteAvoidanceAreaList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_avoidance_area.deserialize_json(item))
    return out
