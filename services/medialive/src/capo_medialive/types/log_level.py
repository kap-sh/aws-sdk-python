"""Generated from Smithy shape ``com.amazonaws.medialive#LogLevel``."""

from typing import Literal, TypeAlias, cast

"""The log level the user wants for their channel."""
LogLevel: TypeAlias = Literal[
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LogLevel) -> str:
    return value


def deserialize_json(data: str) -> LogLevel:
    return cast(LogLevel, data)
