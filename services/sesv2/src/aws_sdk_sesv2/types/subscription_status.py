"""Generated from Smithy shape ``com.amazonaws.sesv2#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionStatus: TypeAlias = Literal[
    "OPT_IN",
    "OPT_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionStatus:
    return cast(SubscriptionStatus, data)
