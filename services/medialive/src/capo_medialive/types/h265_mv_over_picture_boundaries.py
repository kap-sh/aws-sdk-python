"""Generated from Smithy shape ``com.amazonaws.medialive#H265MvOverPictureBoundaries``."""

from typing import Literal, TypeAlias, cast

"""H265 Mv Over Picture Boundaries"""
H265MvOverPictureBoundaries: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265MvOverPictureBoundaries) -> str:
    return value


def deserialize_json(data: str) -> H265MvOverPictureBoundaries:
    return cast(H265MvOverPictureBoundaries, data)
