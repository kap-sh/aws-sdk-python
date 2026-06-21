"""Generated from Smithy shape ``com.amazonaws.iot#LogLevel``."""

from typing import Literal, TypeAlias, cast

LogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "ERROR",
    "WARN",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    return cast(LogLevel, data)
