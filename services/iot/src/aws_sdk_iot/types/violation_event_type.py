"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ViolationEventType: TypeAlias = Literal[
    "in-alarm",
    "alarm-cleared",
    "alarm-invalidated",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "in-alarm",
        "alarm-cleared",
        "alarm-invalidated",
    )
)


def serialize_json(value: ViolationEventType) -> str:
    return value


def deserialize_json(data: str) -> ViolationEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ViolationEventType value: {data!r}")
    return cast(ViolationEventType, data)
