"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentSiteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_payment_site

RouteTollPaymentSiteList: TypeAlias = list[
    "capo_geo_routes.types.route_toll_payment_site.RouteTollPaymentSite"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentSiteList) -> list:
    import capo_geo_routes.types.route_toll_payment_site

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_toll_payment_site.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollPaymentSiteList:
    import capo_geo_routes.types.route_toll_payment_site

    out: RouteTollPaymentSiteList = []
    for item in data:
        out.append(capo_geo_routes.types.route_toll_payment_site.deserialize_json(item))
    return out
