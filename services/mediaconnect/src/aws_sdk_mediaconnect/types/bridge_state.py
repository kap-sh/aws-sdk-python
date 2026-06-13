"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: BridgeState) -> str:
    return value


def deserialize_json(data: str) -> BridgeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BridgeState value: {data!r}")
    return cast(BridgeState, data)
