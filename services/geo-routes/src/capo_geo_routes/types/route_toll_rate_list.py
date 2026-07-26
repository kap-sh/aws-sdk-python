"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollRateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_rate

RouteTollRateList: TypeAlias = list[
    "capo_geo_routes.types.route_toll_rate.RouteTollRate"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollRateList) -> list:
    import capo_geo_routes.types.route_toll_rate

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_toll_rate.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollRateList:
    import capo_geo_routes.types.route_toll_rate

    out: RouteTollRateList = []
    for item in data:
        out.append(capo_geo_routes.types.route_toll_rate.deserialize_json(item))
    return out
