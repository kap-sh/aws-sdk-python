"""Generated from Smithy shape ``com.amazonaws.medialive#H264ParControl``."""

from typing import Literal, TypeAlias, cast

"""H264 Par Control"""
H264ParControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ParControl) -> str:
    return value


def deserialize_json(data: str) -> H264ParControl:
    return cast(H264ParControl, data)
