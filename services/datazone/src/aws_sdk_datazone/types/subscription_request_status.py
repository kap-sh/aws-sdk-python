"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequestStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionRequestStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionRequestStatus:
    return cast(SubscriptionRequestStatus, data)
