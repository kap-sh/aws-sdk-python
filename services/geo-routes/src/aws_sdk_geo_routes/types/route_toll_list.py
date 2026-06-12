"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_toll

RouteTollList: TypeAlias = list["aws_sdk_geo_routes.types.route_toll.RouteToll"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollList) -> list:
    import aws_sdk_geo_routes.types.route_toll

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_toll.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollList:
    import aws_sdk_geo_routes.types.route_toll

    out: RouteTollList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_toll.deserialize_json(item))
    return out
