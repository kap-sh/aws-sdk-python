"""Generated from Smithy shape ``com.amazonaws.greengrass#LoggerLevel``."""

from typing import Literal, TypeAlias, cast

LoggerLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: LoggerLevel) -> str:
    return value


def deserialize_json(data: str) -> LoggerLevel:
    return cast(LoggerLevel, data)
