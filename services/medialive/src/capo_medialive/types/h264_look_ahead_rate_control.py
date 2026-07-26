"""Generated from Smithy shape ``com.amazonaws.medialive#H264LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

"""H264 Look Ahead Rate Control"""
H264LookAheadRateControl: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> H264LookAheadRateControl:
    return cast(H264LookAheadRateControl, data)
