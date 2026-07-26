"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StandardIdentifier``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: StandardIdentifier) -> str:
    return value


def deserialize_json(data: str) -> StandardIdentifier:
    return cast(StandardIdentifier, data)
