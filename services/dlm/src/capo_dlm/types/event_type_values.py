"""Generated from Smithy shape ``com.amazonaws.dlm#EventTypeValues``."""

from typing import Literal, TypeAlias, cast

EventTypeValues: TypeAlias = Literal["shareSnapshot",]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypeValues) -> str:
    return value


def deserialize_json(data: str) -> EventTypeValues:
    return cast(EventTypeValues, data)
