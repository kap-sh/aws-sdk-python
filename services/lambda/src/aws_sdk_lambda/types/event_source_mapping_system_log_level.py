"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingSystemLogLevel``."""

from typing import Literal, TypeAlias, cast

EventSourceMappingSystemLogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingSystemLogLevel) -> str:
    return value


def deserialize_json(data: str) -> EventSourceMappingSystemLogLevel:
    return cast(EventSourceMappingSystemLogLevel, data)
