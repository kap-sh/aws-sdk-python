"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenPcmToId3TaggingState``."""

from typing import Literal, TypeAlias, cast

"""State of Nielsen PCM to ID3 tagging"""
NielsenPcmToId3TaggingState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NielsenPcmToId3TaggingState) -> str:
    return value


def deserialize_json(data: str) -> NielsenPcmToId3TaggingState:
    return cast(NielsenPcmToId3TaggingState, data)
