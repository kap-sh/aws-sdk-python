"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiState``."""

from typing import Literal, TypeAlias, cast

NdiState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NdiState) -> str:
    return value


def deserialize_json(data: str) -> NdiState:
    return cast(NdiState, data)
