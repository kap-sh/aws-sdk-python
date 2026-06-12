"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#AllowNotifications``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

AllowNotifications: TypeAlias = Literal[
    "ALL",
    "NONE",
    "FILTERED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NONE",
        "FILTERED",
    )
)


def serialize_json(value: AllowNotifications) -> str:
    return value


def deserialize_json(data: str) -> AllowNotifications:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllowNotifications value: {data!r}")
    return cast(AllowNotifications, data)
