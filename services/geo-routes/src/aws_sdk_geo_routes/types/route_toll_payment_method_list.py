"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentMethodList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_toll_payment_method

RouteTollPaymentMethodList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_toll_payment_method.RouteTollPaymentMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentMethodList) -> list:
    import aws_sdk_geo_routes.types.route_toll_payment_method

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_toll_payment_method.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTollPaymentMethodList:
    import aws_sdk_geo_routes.types.route_toll_payment_method

    out: RouteTollPaymentMethodList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_toll_payment_method.deserialize_json(item)
        )
    return out
