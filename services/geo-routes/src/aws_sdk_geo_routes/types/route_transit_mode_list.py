"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_mode

RouteTransitModeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_mode.RouteTransitMode"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitModeList) -> list:
    import aws_sdk_geo_routes.types.route_transit_mode

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_transit_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitModeList:
    import aws_sdk_geo_routes.types.route_transit_mode

    out: RouteTransitModeList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_transit_mode.deserialize_json(item))
    return out
