"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationRole``."""

from typing import Literal, TypeAlias, cast

NotificationRole: TypeAlias = Literal[
    "PROJECT_OWNER",
    "PROJECT_CONTRIBUTOR",
    "PROJECT_VIEWER",
    "DOMAIN_OWNER",
    "PROJECT_SUBSCRIBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRole) -> str:
    return value


def deserialize_json(data: str) -> NotificationRole:
    return cast(NotificationRole, data)
