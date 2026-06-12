"""Generated from Smithy shape ``com.amazonaws.iotevents#LoggingLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

LoggingLevel: TypeAlias = Literal[
    "ERROR",
    "INFO",
    "DEBUG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "INFO",
        "DEBUG",
    )
)


def serialize_json(value: LoggingLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggingLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggingLevel value: {data!r}")
    return cast(LoggingLevel, data)
