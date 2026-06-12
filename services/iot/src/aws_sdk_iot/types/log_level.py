"""Generated from Smithy shape ``com.amazonaws.iot#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "ERROR",
    "WARN",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEBUG",
        "INFO",
        "ERROR",
        "WARN",
        "DISABLED",
    )
)


def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
