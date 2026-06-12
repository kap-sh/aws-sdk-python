"""Generated from Smithy shape ``com.amazonaws.mediapackage#PlaylistType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage.errors import DeserializationError

PlaylistType: TypeAlias = Literal[
    "NONE",
    "EVENT",
    "VOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "EVENT",
        "VOD",
    )
)


def serialize_json(value: PlaylistType) -> str:
    return value


def deserialize_json(data: str) -> PlaylistType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlaylistType value: {data!r}")
    return cast(PlaylistType, data)
