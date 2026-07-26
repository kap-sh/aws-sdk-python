"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "DEBUG",
    "ERROR",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    return cast(LogLevel, data)
