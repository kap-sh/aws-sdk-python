"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

NotificationRole: TypeAlias = Literal[
    "PROJECT_OWNER",
    "PROJECT_CONTRIBUTOR",
    "PROJECT_VIEWER",
    "DOMAIN_OWNER",
    "PROJECT_SUBSCRIBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROJECT_OWNER",
        "PROJECT_CONTRIBUTOR",
        "PROJECT_VIEWER",
        "DOMAIN_OWNER",
        "PROJECT_SUBSCRIBER",
    )
)


def serialize_json(value: NotificationRole) -> str:
    return value


def deserialize_json(data: str) -> NotificationRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationRole value: {data!r}")
    return cast(NotificationRole, data)
