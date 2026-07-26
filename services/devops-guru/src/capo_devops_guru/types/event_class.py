"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventClass``."""

from typing import Literal, TypeAlias, cast

EventClass: TypeAlias = Literal[
    "INFRASTRUCTURE",
    "DEPLOYMENT",
    "SECURITY_CHANGE",
    "CONFIG_CHANGE",
    "SCHEMA_CHANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventClass) -> str:
    return value


def deserialize_json(data: str) -> EventClass:
    return cast(EventClass, data)
