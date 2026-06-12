"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothAudioDeduplication``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream."""
MsSmoothAudioDeduplication: TypeAlias = Literal[
    "COMBINE_DUPLICATE_STREAMS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMBINE_DUPLICATE_STREAMS",
        "NONE",
    )
)


def serialize_json(value: MsSmoothAudioDeduplication) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothAudioDeduplication:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MsSmoothAudioDeduplication value: {data!r}"
        )
    return cast(MsSmoothAudioDeduplication, data)
