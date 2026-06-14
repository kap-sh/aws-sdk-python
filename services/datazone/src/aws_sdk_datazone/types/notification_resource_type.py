"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

NotificationResourceType: TypeAlias = Literal["PROJECT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROJECT",))


def serialize_json(value: NotificationResourceType) -> str:
    return value


def deserialize_json(data: str) -> NotificationResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationResourceType value: {data!r}")
    return cast(NotificationResourceType, data)
