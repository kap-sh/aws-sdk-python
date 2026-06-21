"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeState``."""

from typing import Literal, TypeAlias, cast

ProbeState: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
    "ERROR",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProbeState) -> str:
    return value


def deserialize_json(data: str) -> ProbeState:
    return cast(ProbeState, data)
