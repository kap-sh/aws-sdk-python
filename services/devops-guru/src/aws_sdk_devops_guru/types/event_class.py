"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

EventClass: TypeAlias = Literal[
    "INFRASTRUCTURE",
    "DEPLOYMENT",
    "SECURITY_CHANGE",
    "CONFIG_CHANGE",
    "SCHEMA_CHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFRASTRUCTURE",
        "DEPLOYMENT",
        "SECURITY_CHANGE",
        "CONFIG_CHANGE",
        "SCHEMA_CHANGE",
    )
)


def serialize_json(value: EventClass) -> str:
    return value


def deserialize_json(data: str) -> EventClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventClass value: {data!r}")
    return cast(EventClass, data)
