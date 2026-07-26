"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteResponseNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_response_notice

RouteResponseNoticeList: TypeAlias = list[
    "capo_geo_routes.types.route_response_notice.RouteResponseNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteResponseNoticeList) -> list:
    import capo_geo_routes.types.route_response_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_response_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteResponseNoticeList:
    import capo_geo_routes.types.route_response_notice

    out: RouteResponseNoticeList = []
    for item in data:
        out.append(capo_geo_routes.types.route_response_notice.deserialize_json(item))
    return out
