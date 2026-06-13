"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Status: TypeAlias = Literal[
    "STANDBY",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "STARTING",
    "STOPPING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDBY",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "STARTING",
        "STOPPING",
        "ERROR",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
