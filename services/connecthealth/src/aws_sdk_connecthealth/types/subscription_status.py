"""Generated from Smithy shape ``com.amazonaws.connecthealth#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    return cast(SubscriptionStatus, data)
