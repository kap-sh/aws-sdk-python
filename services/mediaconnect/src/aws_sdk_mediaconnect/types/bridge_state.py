"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeState``."""

from typing import Literal, TypeAlias, cast

BridgeState: TypeAlias = Literal[
    "CREATING",
    "STANDBY",
    "STARTING",
    "DEPLOYING",
    "ACTIVE",
    "STOPPING",
    "DELETING",
    "DELETED",
    "START_FAILED",
    "START_PENDING",
    "STOP_FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: BridgeState) -> str:
    return value


def deserialize_json(data: str) -> BridgeState:
    return cast(BridgeState, data)
