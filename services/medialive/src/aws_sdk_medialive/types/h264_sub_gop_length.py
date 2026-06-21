"""Generated from Smithy shape ``com.amazonaws.medialive#H264SubGopLength``."""

from typing import Literal, TypeAlias, cast

"""H264 Sub Gop Length"""
H264SubGopLength: TypeAlias = Literal[
    "DYNAMIC",
    "FIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> H264SubGopLength:
    return cast(H264SubGopLength, data)
