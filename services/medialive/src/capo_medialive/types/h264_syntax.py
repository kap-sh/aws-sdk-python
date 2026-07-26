"""Generated from Smithy shape ``com.amazonaws.medialive#H264Syntax``."""

from typing import Literal, TypeAlias, cast

"""H264 Syntax"""
H264Syntax: TypeAlias = Literal[
    "DEFAULT",
    "RP2027",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264Syntax) -> str:
    return value


def deserialize_json(data: str) -> H264Syntax:
    return cast(H264Syntax, data)
