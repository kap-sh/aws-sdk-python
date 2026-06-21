"""Generated from Smithy shape ``com.amazonaws.medialive#H264GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""H264 Gop Size Units"""
H264GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> H264GopSizeUnits:
    return cast(H264GopSizeUnits, data)
