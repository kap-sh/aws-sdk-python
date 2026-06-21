"""Generated from Smithy shape ``com.amazonaws.lambda#SystemLogLevel``."""

from typing import Literal, TypeAlias, cast

SystemLogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemLogLevel) -> str:
    return value


def deserialize_json(data: str) -> SystemLogLevel:
    return cast(SystemLogLevel, data)
