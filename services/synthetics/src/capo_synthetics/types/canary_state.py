"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryState``."""

from typing import Literal, TypeAlias, cast

CanaryState: TypeAlias = Literal[
    "CREATING",
    "READY",
    "STARTING",
    "RUNNING",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "ERROR",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryState) -> str:
    return value


def deserialize_json(data: str) -> CanaryState:
    return cast(CanaryState, data)
