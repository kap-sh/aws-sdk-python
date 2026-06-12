"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_leg

RouteLegList: TypeAlias = list["aws_sdk_geo_routes.types.route_leg.RouteLeg"]


# --- restJson1 ser/de ---
def serialize_json(value: RouteLegList) -> list:
    import aws_sdk_geo_routes.types.route_leg

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_leg.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteLegList:
    import aws_sdk_geo_routes.types.route_leg

    out: RouteLegList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_leg.deserialize_json(item))
    return out
