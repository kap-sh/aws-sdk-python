"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

LogLevel: TypeAlias = Literal[
    "DEBUG",
    "ERROR",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEBUG",
        "ERROR",
        "INFO",
        "WARN",
    )
)


def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogLevel value: {data!r}")
    return cast(LogLevel, data)
