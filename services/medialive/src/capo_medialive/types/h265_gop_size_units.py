"""Generated from Smithy shape ``com.amazonaws.medialive#H265GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""H265 Gop Size Units"""
H265GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> H265GopSizeUnits:
    return cast(H265GopSizeUnits, data)
