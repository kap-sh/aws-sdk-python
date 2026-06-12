"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_zone

RouteZoneList: TypeAlias = list["aws_sdk_geo_routes.types.route_zone.RouteZone"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteZoneList) -> list:
    import aws_sdk_geo_routes.types.route_zone

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_zone.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteZoneList:
    import aws_sdk_geo_routes.types.route_zone

    out: RouteZoneList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_zone.deserialize_json(item))
    return out
