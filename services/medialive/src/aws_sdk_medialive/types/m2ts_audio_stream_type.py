"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioStreamType``."""

from typing import Literal, TypeAlias, cast

"""M2ts Audio Stream Type"""
M2tsAudioStreamType: TypeAlias = Literal[
    "ATSC",
    "DVB",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAudioStreamType) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioStreamType:
    return cast(M2tsAudioStreamType, data)
