"""Generated from Smithy shape ``com.amazonaws.iotevents#PayloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

PayloadType: TypeAlias = Literal[
    "STRING",
    "JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "JSON",
    )
)


def serialize_json(value: PayloadType) -> str:
    return value


def deserialize_json(data: str) -> PayloadType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PayloadType value: {data!r}")
    return cast(PayloadType, data)
