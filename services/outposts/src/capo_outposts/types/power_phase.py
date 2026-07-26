"""Generated from Smithy shape ``com.amazonaws.outposts#PowerPhase``."""

from typing import Literal, TypeAlias, cast

PowerPhase: TypeAlias = Literal[
    "SINGLE_PHASE",
    "THREE_PHASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PowerPhase) -> str:
    return value


def deserialize_json(data: str) -> PowerPhase:
    return cast(PowerPhase, data)
