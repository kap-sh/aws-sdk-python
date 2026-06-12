"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteWebLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_web_link

RouteWebLinkList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_web_link.RouteWebLink"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteWebLinkList) -> list:
    import aws_sdk_geo_routes.types.route_web_link

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_web_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteWebLinkList:
    import aws_sdk_geo_routes.types.route_web_link

    out: RouteWebLinkList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_web_link.deserialize_json(item))
    return out
