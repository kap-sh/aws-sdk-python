"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteResponseNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_response_notice

RouteResponseNoticeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_response_notice.RouteResponseNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteResponseNoticeList) -> list:
    import aws_sdk_geo_routes.types.route_response_notice

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.route_response_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteResponseNoticeList:
    import aws_sdk_geo_routes.types.route_response_notice

    out: RouteResponseNoticeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_response_notice.deserialize_json(item)
        )
    return out
