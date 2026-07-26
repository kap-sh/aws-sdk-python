"""Generated from Smithy shape ``com.amazonaws.medialive#HlsTsFileMode``."""

from typing import Literal, TypeAlias, cast

"""Hls Ts File Mode"""
HlsTsFileMode: TypeAlias = Literal[
    "SEGMENTED_FILES",
    "SINGLE_FILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsTsFileMode) -> str:
    return value


def deserialize_json(data: str) -> HlsTsFileMode:
    return cast(HlsTsFileMode, data)
