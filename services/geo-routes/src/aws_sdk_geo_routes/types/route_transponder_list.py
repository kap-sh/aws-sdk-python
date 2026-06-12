"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransponderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transponder

RouteTransponderList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transponder.RouteTransponder"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransponderList) -> list:
    import aws_sdk_geo_routes.types.route_transponder

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_transponder.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransponderList:
    import aws_sdk_geo_routes.types.route_transponder

    out: RouteTransponderList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_transponder.deserialize_json(item))
    return out
