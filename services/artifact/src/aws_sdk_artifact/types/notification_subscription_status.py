"""Generated from Smithy shape ``com.amazonaws.artifact#NotificationSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

NotificationSubscriptionStatus: TypeAlias = Literal[
    "SUBSCRIBED",
    "NOT_SUBSCRIBED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> NotificationSubscriptionStatus:
    return cast(NotificationSubscriptionStatus, data)
