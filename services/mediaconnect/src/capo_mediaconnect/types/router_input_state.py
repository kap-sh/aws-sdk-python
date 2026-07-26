"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputState``."""

from typing import Literal, TypeAlias, cast

RouterInputState: TypeAlias = Literal[
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
def serialize_json(value: RouterInputState) -> str:
    return value


def deserialize_json(data: str) -> RouterInputState:
    return cast(RouterInputState, data)
