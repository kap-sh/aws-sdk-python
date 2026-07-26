"""Generated from Smithy shape ``com.amazonaws.lambda#ApplicationLogLevel``."""

from typing import Literal, TypeAlias, cast

ApplicationLogLevel: TypeAlias = Literal[
    "TRACE",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationLogLevel) -> str:
    return value


def deserialize_json(data: str) -> ApplicationLogLevel:
    return cast(ApplicationLogLevel, data)
