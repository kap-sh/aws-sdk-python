"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationMessageType``."""

from typing import Literal, TypeAlias, cast

NotificationMessageType: TypeAlias = Literal[
    "NEW_INSIGHT",
    "CLOSED_INSIGHT",
    "NEW_ASSOCIATION",
    "SEVERITY_UPGRADED",
    "NEW_RECOMMENDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationMessageType) -> str:
    return value


def deserialize_json(data: str) -> NotificationMessageType:
    return cast(NotificationMessageType, data)
