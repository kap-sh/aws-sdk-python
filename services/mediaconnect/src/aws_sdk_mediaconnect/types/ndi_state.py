"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

NdiState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: NdiState) -> str:
    return value


def deserialize_json(data: str) -> NdiState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NdiState value: {data!r}")
    return cast(NdiState, data)
