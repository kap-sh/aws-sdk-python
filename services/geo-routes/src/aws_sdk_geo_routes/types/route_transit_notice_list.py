"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_notice

RouteTransitNoticeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_notice.RouteTransitNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNoticeList) -> list:
    import aws_sdk_geo_routes.types.route_transit_notice

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_transit_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTransitNoticeList:
    import aws_sdk_geo_routes.types.route_transit_notice

    out: RouteTransitNoticeList = []
    for item in data:
        out.append(aws_sdk_geo_routes.types.route_transit_notice.deserialize_json(item))
    return out
