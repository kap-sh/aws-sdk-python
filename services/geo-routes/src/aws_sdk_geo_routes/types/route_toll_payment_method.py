"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "BankCard",
        "Cash",
        "CashExact",
        "CreditCard",
        "PassSubscription",
        "TravelCard",
        "Transponder",
        "VideoToll",
    )
)


def serialize_json(value: RouteTollPaymentMethod) -> str:
    return value


def deserialize_json(data: str) -> RouteTollPaymentMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTollPaymentMethod value: {data!r}")
    return cast(RouteTollPaymentMethod, data)
