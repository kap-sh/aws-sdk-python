"""Generated from Smithy shape ``com.amazonaws.dlm#EventSourceValues``."""

from typing import Literal, TypeAlias, cast

EventSourceValues: TypeAlias = Literal["MANAGED_CWE",]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceValues) -> str:
    return value


def deserialize_json(data: str) -> EventSourceValues:
    return cast(EventSourceValues, data)
