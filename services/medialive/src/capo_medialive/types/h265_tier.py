"""Generated from Smithy shape ``com.amazonaws.medialive#H265Tier``."""

from typing import Literal, TypeAlias, cast

"""H265 Tier"""
H265Tier: TypeAlias = Literal[
    "HIGH",
    "MAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Tier) -> str:
    return value


def deserialize_json(data: str) -> H265Tier:
    return cast(H265Tier, data)
