"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiNoticeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_notice

RouteTaxiNoticeList: TypeAlias = list[
    "capo_geo_routes.types.route_taxi_notice.RouteTaxiNotice"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiNoticeList) -> list:
    import capo_geo_routes.types.route_taxi_notice

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_taxi_notice.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTaxiNoticeList:
    import capo_geo_routes.types.route_taxi_notice

    out: RouteTaxiNoticeList = []
    for item in data:
        out.append(capo_geo_routes.types.route_taxi_notice.deserialize_json(item))
    return out
