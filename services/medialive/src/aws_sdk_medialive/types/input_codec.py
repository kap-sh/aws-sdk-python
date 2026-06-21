"""Generated from Smithy shape ``com.amazonaws.medialive#InputCodec``."""

from typing import Literal, TypeAlias, cast

"""codec in increasing order of complexity"""
InputCodec: TypeAlias = Literal[
    "MPEG2",
    "AVC",
    "HEVC",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputCodec) -> str:
    return value


def deserialize_json(data: str) -> InputCodec:
    return cast(InputCodec, data)
