"""Generated from Smithy shape ``com.amazonaws.qbusiness#AutoSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

AutoSubscriptionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoSubscriptionStatus:
    return cast(AutoSubscriptionStatus, data)
