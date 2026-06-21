"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Tiles``."""

from typing import Literal, TypeAlias, cast

"""Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures."""
H265Tiles: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Tiles) -> str:
    return value


def deserialize_json(data: str) -> H265Tiles:
    return cast(H265Tiles, data)
