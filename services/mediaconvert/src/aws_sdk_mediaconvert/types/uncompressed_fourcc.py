"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedFourcc``."""

from typing import Literal, TypeAlias, cast

"""The four character code for the uncompressed video."""
UncompressedFourcc: TypeAlias = Literal[
    "I420",
    "I422",
    "I444",
]


# --- restJson1 ser/de ---
def serialize_json(value: UncompressedFourcc) -> str:
    return value


def deserialize_json(data: str) -> UncompressedFourcc:
    return cast(UncompressedFourcc, data)
