"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouterOutputState) -> str:
    return value


def deserialize_json(data: str) -> RouterOutputState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterOutputState value: {data!r}")
    return cast(RouterOutputState, data)
