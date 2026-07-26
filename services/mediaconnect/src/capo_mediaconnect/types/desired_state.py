"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DesiredState``."""

from typing import Literal, TypeAlias, cast

DesiredState: TypeAlias = Literal[
    "ACTIVE",
    "STANDBY",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DesiredState) -> str:
    return value


def deserialize_json(data: str) -> DesiredState:
    return cast(DesiredState, data)
