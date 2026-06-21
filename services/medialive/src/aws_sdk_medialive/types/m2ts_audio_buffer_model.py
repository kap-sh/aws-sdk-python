"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioBufferModel``."""

from typing import Literal, TypeAlias, cast

"""M2ts Audio Buffer Model"""
M2tsAudioBufferModel: TypeAlias = Literal[
    "ATSC",
    "DVB",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAudioBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioBufferModel:
    return cast(M2tsAudioBufferModel, data)
