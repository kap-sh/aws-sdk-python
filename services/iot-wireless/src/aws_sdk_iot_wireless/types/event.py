"""Generated from Smithy shape ``com.amazonaws.iotwireless#Event``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>Sidewalk device status notification.</p>"""
Event: TypeAlias = Literal[
    "discovered",
    "lost",
    "ack",
    "nack",
    "passthrough",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "discovered",
        "lost",
        "ack",
        "nack",
        "passthrough",
    )
)


def serialize_json(value: Event) -> str:
    return value


def deserialize_json(data: str) -> Event:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Event value: {data!r}")
    return cast(Event, data)
