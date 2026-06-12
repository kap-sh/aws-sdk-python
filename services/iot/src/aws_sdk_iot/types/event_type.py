"""Generated from Smithy shape ``com.amazonaws.iot#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

EventType: TypeAlias = Literal[
    "THING",
    "THING_GROUP",
    "THING_TYPE",
    "THING_GROUP_MEMBERSHIP",
    "THING_GROUP_HIERARCHY",
    "THING_TYPE_ASSOCIATION",
    "JOB",
    "JOB_EXECUTION",
    "POLICY",
    "CERTIFICATE",
    "CA_CERTIFICATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "THING",
        "THING_GROUP",
        "THING_TYPE",
        "THING_GROUP_MEMBERSHIP",
        "THING_GROUP_HIERARCHY",
        "THING_TYPE_ASSOCIATION",
        "JOB",
        "JOB_EXECUTION",
        "POLICY",
        "CERTIFICATE",
        "CA_CERTIFICATE",
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
