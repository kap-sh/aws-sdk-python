"""Generated from Smithy shape ``com.amazonaws.devopsguru#NotificationMessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

NotificationMessageType: TypeAlias = Literal[
    "NEW_INSIGHT",
    "CLOSED_INSIGHT",
    "NEW_ASSOCIATION",
    "SEVERITY_UPGRADED",
    "NEW_RECOMMENDATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEW_INSIGHT",
        "CLOSED_INSIGHT",
        "NEW_ASSOCIATION",
        "SEVERITY_UPGRADED",
        "NEW_RECOMMENDATION",
    )
)


def serialize_json(value: NotificationMessageType) -> str:
    return value


def deserialize_json(data: str) -> NotificationMessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationMessageType value: {data!r}")
    return cast(NotificationMessageType, data)
