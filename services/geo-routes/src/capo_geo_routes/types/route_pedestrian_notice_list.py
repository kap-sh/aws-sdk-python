"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_pedestrian_notice

RoutePedestrianNoticeList: TypeAlias = list[
    "capo_geo_routes.types.route_pedestrian_notice.RoutePedestrianNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianNoticeList) -> list:
    import capo_geo_routes.types.route_pedestrian_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_pedestrian_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutePedestrianNoticeList:
    import capo_geo_routes.types.route_pedestrian_notice

    out: RoutePedestrianNoticeList = []
    for item in data:
        out.append(capo_geo_routes.types.route_pedestrian_notice.deserialize_json(item))
    return out
