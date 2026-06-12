"""Generated from Smithy shape ``com.amazonaws.medialive#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The log level the user wants for their channel."""
LogLevel: TypeAlias = Literal[
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "WARNING",
        "INFO",
        "DEBUG",
        "DISABLED",
    )
)


def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
