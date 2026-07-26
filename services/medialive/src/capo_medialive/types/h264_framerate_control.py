"""Generated from Smithy shape ``com.amazonaws.medialive#H264FramerateControl``."""

from typing import Literal, TypeAlias, cast

"""H264 Framerate Control"""
H264FramerateControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264FramerateControl) -> str:
    return value


def deserialize_json(data: str) -> H264FramerateControl:
    return cast(H264FramerateControl, data)
