"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAttributionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_attribution

RouteAttributionList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_attribution.RouteAttribution"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAttributionList) -> list:
    import aws_sdk_geo_routes.types.route_attribution

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_attribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteAttributionList:
    import aws_sdk_geo_routes.types.route_attribution

    out: RouteAttributionList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_attribution.deserialize_json(item))
    return out
