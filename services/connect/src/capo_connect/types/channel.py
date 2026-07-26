"""Generated from Smithy shape ``com.amazonaws.connect#Channel``."""

from typing import Literal, TypeAlias, cast

Channel: TypeAlias = Literal[
    "VOICE",
    "CHAT",
    "TASK",
    "EMAIL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Channel) -> str:
    return value


def deserialize_json(data: str) -> Channel:
    return cast(Channel, data)
