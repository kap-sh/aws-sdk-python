"""Generated from Smithy shape ``com.amazonaws.groundstation#FrequencyUnits``."""

from typing import Literal, TypeAlias, cast

FrequencyUnits: TypeAlias = Literal[
    "GHz",
    "MHz",
    "kHz",
]


# --- restJson1 ser/de ---
def serialize_json(value: FrequencyUnits) -> str:
    return value


def deserialize_json(data: str) -> FrequencyUnits:
    return cast(FrequencyUnits, data)
