"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DesiredState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

DesiredState: TypeAlias = Literal[
    "ACTIVE",
    "STANDBY",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "STANDBY",
        "DELETED",
    )
)


def serialize_json(value: DesiredState) -> str:
    return value


def deserialize_json(data: str) -> DesiredState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DesiredState value: {data!r}")
    return cast(DesiredState, data)
