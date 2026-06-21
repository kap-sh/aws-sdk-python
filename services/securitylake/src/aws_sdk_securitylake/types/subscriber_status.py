"""Generated from Smithy shape ``com.amazonaws.securitylake#SubscriberStatus``."""

from typing import Literal, TypeAlias, cast

SubscriberStatus: TypeAlias = Literal[
    "ACTIVE",
    "DEACTIVATED",
    "PENDING",
    "READY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriberStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriberStatus:
    return cast(SubscriberStatus, data)
