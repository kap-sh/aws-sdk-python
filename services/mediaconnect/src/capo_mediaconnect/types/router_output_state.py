"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputState``."""

from typing import Literal, TypeAlias, cast

RouterOutputState: TypeAlias = Literal[
    "CREATING",
    "STANDBY",
    "STARTING",
    "ACTIVE",
    "STOPPING",
    "DELETING",
    "UPDATING",
    "ERROR",
    "RECOVERING",
    "MIGRATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputState) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputState:
    return cast(RouterOutputState, data)
