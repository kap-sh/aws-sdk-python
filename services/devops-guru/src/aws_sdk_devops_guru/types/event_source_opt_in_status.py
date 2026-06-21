"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventSourceOptInStatus``."""

from typing import Literal, TypeAlias, cast

EventSourceOptInStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceOptInStatus) -> str:
    return value


def deserialize_json(data: str) -> EventSourceOptInStatus:
    return cast(EventSourceOptInStatus, data)
