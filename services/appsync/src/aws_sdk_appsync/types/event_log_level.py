"""Generated from Smithy shape ``com.amazonaws.appsync#EventLogLevel``."""

from typing import Literal, TypeAlias, cast

EventLogLevel: TypeAlias = Literal[
    "NONE",
    "ERROR",
    "ALL",
    "INFO",
    "DEBUG",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventLogLevel) -> str:
    return value


def deserialize_json(data: str) -> EventLogLevel:
    return cast(EventLogLevel, data)
