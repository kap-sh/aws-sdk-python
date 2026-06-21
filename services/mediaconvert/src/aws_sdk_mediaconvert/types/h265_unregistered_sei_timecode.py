"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265UnregisteredSeiTimecode``."""

from typing import Literal, TypeAlias, cast

"""Inserts timecode for each frame as 4 bytes of an unregistered SEI message."""
H265UnregisteredSeiTimecode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265UnregisteredSeiTimecode) -> str:
    return value


def deserialize_json(data: str) -> H265UnregisteredSeiTimecode:
    return cast(H265UnregisteredSeiTimecode, data)
