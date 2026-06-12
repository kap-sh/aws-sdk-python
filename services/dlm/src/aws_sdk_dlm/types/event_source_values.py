"""Generated from Smithy shape ``com.amazonaws.dlm#EventSourceValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

EventSourceValues: TypeAlias = Literal["MANAGED_CWE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MANAGED_CWE",))


def serialize_json(value: EventSourceValues) -> str:
    return value


def deserialize_json(data: str) -> EventSourceValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceValues value: {data!r}")
    return cast(EventSourceValues, data)
