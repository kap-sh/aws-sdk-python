"""Generated from Smithy shape ``com.amazonaws.medialive#H265Profile``."""

from typing import Literal, TypeAlias, cast

"""H265 Profile"""
H265Profile: TypeAlias = Literal[
    "MAIN",
    "MAIN_10BIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Profile) -> str:
    return value


def deserialize_json(data: str) -> H265Profile:
    return cast(H265Profile, data)
