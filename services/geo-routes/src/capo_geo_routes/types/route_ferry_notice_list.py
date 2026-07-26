"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_notice

RouteFerryNoticeList: TypeAlias = list[
    "capo_geo_routes.types.route_ferry_notice.RouteFerryNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryNoticeList) -> list:
    import capo_geo_routes.types.route_ferry_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_ferry_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteFerryNoticeList:
    import capo_geo_routes.types.route_ferry_notice

    out: RouteFerryNoticeList = []
    for item in data:
        out.append(capo_geo_routes.types.route_ferry_notice.deserialize_json(item))
    return out
