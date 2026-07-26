"""Generated from Smithy shape ``com.amazonaws.medialive#H265TilePadding``."""

from typing import Literal, TypeAlias, cast

"""H265 Tile Padding"""
H265TilePadding: TypeAlias = Literal[
    "NONE",
    "PADDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265TilePadding) -> str:
    return value


def deserialize_json(data: str) -> H265TilePadding:
    return cast(H265TilePadding, data)
