"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

LoggerLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEBUG",
        "INFO",
        "WARN",
        "ERROR",
        "FATAL",
    )
)


def serialize_json(value: LoggerLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggerLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoggerLevel value: {data!r}")
    return cast(LoggerLevel, data)
