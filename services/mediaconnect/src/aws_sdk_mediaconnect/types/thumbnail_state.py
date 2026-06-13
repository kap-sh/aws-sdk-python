"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ThumbnailState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ThumbnailState: TypeAlias = Literal[
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


def serialize_json(value: ThumbnailState) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThumbnailState value: {data!r}")
    return cast(ThumbnailState, data)
