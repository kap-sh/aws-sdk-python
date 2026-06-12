"""Generated from Smithy shape ``com.amazonaws.iot#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "MQTT",
    "HTTP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MQTT",
        "HTTP",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
