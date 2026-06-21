"""Generated from Smithy shape ``com.amazonaws.ivs#TranscodePreset``."""

from typing import Literal, TypeAlias, cast

TranscodePreset: TypeAlias = Literal[
    "HIGHER_BANDWIDTH_DELIVERY",
    "CONSTRAINED_BANDWIDTH_DELIVERY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscodePreset) -> str:
    return value


def deserialize_json(data: str) -> TranscodePreset:
    return cast(TranscodePreset, data)
