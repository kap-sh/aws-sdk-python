"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentMethod``."""

from typing import Literal, TypeAlias, cast

RouteTollPaymentMethod: TypeAlias = Literal[
    "BankCard",
    "Cash",
    "CashExact",
    "CreditCard",
    "PassSubscription",
    "TravelCard",
    "Transponder",
    "VideoToll",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentMethod) -> str:
    return value


def deserialize_json(data: str) -> RouteTollPaymentMethod:
    return cast(RouteTollPaymentMethod, data)
