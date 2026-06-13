"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

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


def serialize_json(value: RouterInputState) -> str:
    return value


def deserialize_json(data: str) -> RouterInputState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouterInputState value: {data!r}")
    return cast(RouterInputState, data)
