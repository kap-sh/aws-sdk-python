"""Generated from Smithy shape ``com.amazonaws.outposts#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

SubscriptionType: TypeAlias = Literal[
    "ORIGINAL",
    "RENEWAL",
    "CAPACITY_INCREASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    return cast(SubscriptionType, data)
