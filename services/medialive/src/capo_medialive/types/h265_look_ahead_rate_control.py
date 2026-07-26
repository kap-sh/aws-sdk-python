"""Generated from Smithy shape ``com.amazonaws.medialive#H265LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

"""H265 Look Ahead Rate Control"""
H265LookAheadRateControl: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> H265LookAheadRateControl:
    return cast(H265LookAheadRateControl, data)
