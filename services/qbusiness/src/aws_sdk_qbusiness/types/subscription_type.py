"""Generated from Smithy shape ``com.amazonaws.qbusiness#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

SubscriptionType: TypeAlias = Literal[
    "Q_LITE",
    "Q_BUSINESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    return cast(SubscriptionType, data)
