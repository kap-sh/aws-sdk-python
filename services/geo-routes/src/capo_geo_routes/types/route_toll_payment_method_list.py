"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentMethodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_payment_method

RouteTollPaymentMethodList: TypeAlias = list[
    "capo_geo_routes.types.route_toll_payment_method.RouteTollPaymentMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentMethodList) -> list:
    import capo_geo_routes.types.route_toll_payment_method

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_toll_payment_method.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTollPaymentMethodList:
    import capo_geo_routes.types.route_toll_payment_method

    out: RouteTollPaymentMethodList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_toll_payment_method.deserialize_json(item)
        )
    return out
