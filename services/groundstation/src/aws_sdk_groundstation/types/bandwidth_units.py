"""Generated from Smithy shape ``com.amazonaws.groundstation#BandwidthUnits``."""

from typing import Literal, TypeAlias, cast

BandwidthUnits: TypeAlias = Literal[
    "GHz",
    "MHz",
    "kHz",
]


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthUnits) -> str:
    return value


def deserialize_json(data: str) -> BandwidthUnits:
    return cast(BandwidthUnits, data)
