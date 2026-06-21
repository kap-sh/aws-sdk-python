"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringState``."""

from typing import Literal, TypeAlias, cast

PeeringState: TypeAlias = Literal[
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeeringState) -> str:
    return value


def deserialize_json(data: str) -> PeeringState:
    return cast(PeeringState, data)
