"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264UnregisteredSeiTimecode``."""

from typing import Literal, TypeAlias, cast

"""Inserts timecode for each frame as 4 bytes of an unregistered SEI message."""
H264UnregisteredSeiTimecode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264UnregisteredSeiTimecode) -> str:
    return value


def deserialize_json(data: str) -> H264UnregisteredSeiTimecode:
    return cast(H264UnregisteredSeiTimecode, data)
