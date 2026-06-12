"""Generated from Smithy shape ``com.amazonaws.connect#NotificationContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

NotificationContentType: TypeAlias = Literal["PLAIN_TEXT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PLAIN_TEXT",))


def serialize_json(value: NotificationContentType) -> str:
    return value


def deserialize_json(data: str) -> NotificationContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationContentType value: {data!r}")
    return cast(NotificationContentType, data)
