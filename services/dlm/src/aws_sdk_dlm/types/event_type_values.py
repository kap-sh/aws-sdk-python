"""Generated from Smithy shape ``com.amazonaws.dlm#EventTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

EventTypeValues: TypeAlias = Literal["shareSnapshot",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("shareSnapshot",))


def serialize_json(value: EventTypeValues) -> str:
    return value


def deserialize_json(data: str) -> EventTypeValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventTypeValues value: {data!r}")
    return cast(EventTypeValues, data)
