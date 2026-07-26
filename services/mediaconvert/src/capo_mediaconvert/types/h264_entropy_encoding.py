"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264EntropyEncoding``."""

from typing import Literal, TypeAlias, cast

"""Entropy encoding mode. Use CABAC (must be in Main or High profile) or CAVLC."""
H264EntropyEncoding: TypeAlias = Literal[
    "CABAC",
    "CAVLC",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264EntropyEncoding) -> str:
    return value


def deserialize_json(data: str) -> H264EntropyEncoding:
    return cast(H264EntropyEncoding, data)
