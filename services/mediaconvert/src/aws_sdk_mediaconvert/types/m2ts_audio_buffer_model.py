"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsAudioBufferModel``."""

from typing import Literal, TypeAlias, cast

"""Selects between the DVB and ATSC buffer models for Dolby Digital audio."""
M2tsAudioBufferModel: TypeAlias = Literal[
    "DVB",
    "ATSC",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAudioBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioBufferModel:
    return cast(M2tsAudioBufferModel, data)
