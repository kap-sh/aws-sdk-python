"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothAudioDeduplication``."""

from typing import Literal, TypeAlias, cast

"""COMBINE_DUPLICATE_STREAMS combines identical audio encoding settings across a Microsoft Smooth output group into a single audio stream."""
MsSmoothAudioDeduplication: TypeAlias = Literal[
    "COMBINE_DUPLICATE_STREAMS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothAudioDeduplication) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothAudioDeduplication:
    return cast(MsSmoothAudioDeduplication, data)
