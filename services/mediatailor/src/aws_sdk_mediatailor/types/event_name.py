"""Generated from Smithy shape ``com.amazonaws.mediatailor#EventName``."""

from typing import Literal, TypeAlias, cast

EventName: TypeAlias = Literal[
    "PRE_SESSION_INITIALIZATION",
    "PRE_ADS_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventName) -> str:
    return value


def deserialize_json(data: str) -> EventName:
    return cast(EventName, data)
