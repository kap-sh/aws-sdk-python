"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StandardIdentifier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

StandardIdentifier: TypeAlias = Literal[
    "PROFILE",
    "ASSET",
    "CASE",
    "DEVICE",
    "WEB_ANALYTICS",
    "ORDER",
    "COMMUNICATION_RECORD",
    "AIR_PREFERENCE",
    "HOTEL_PREFERENCE",
    "AIR_BOOKING",
    "AIR_SEGMENT",
    "HOTEL_RESERVATION",
    "HOTEL_STAY_REVENUE",
    "LOYALTY",
    "LOYALTY_TRANSACTION",
    "LOYALTY_PROMOTION",
    "UNIQUE",
    "SECONDARY",
    "LOOKUP_ONLY",
    "NEW_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE",
        "ASSET",
        "CASE",
        "DEVICE",
        "WEB_ANALYTICS",
        "ORDER",
        "COMMUNICATION_RECORD",
        "AIR_PREFERENCE",
        "HOTEL_PREFERENCE",
        "AIR_BOOKING",
        "AIR_SEGMENT",
        "HOTEL_RESERVATION",
        "HOTEL_STAY_REVENUE",
        "LOYALTY",
        "LOYALTY_TRANSACTION",
        "LOYALTY_PROMOTION",
        "UNIQUE",
        "SECONDARY",
        "LOOKUP_ONLY",
        "NEW_ONLY",
    )
)


def serialize_json(value: StandardIdentifier) -> str:
    return value


def deserialize_json(data: str) -> StandardIdentifier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StandardIdentifier value: {data!r}")
    return cast(StandardIdentifier, data)
