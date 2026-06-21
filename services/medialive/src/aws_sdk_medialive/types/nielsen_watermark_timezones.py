"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarkTimezones``."""

from typing import Literal, TypeAlias, cast

"""Nielsen Watermark Timezones"""
NielsenWatermarkTimezones: TypeAlias = Literal[
    "AMERICA_PUERTO_RICO",
    "US_ALASKA",
    "US_ARIZONA",
    "US_CENTRAL",
    "US_EASTERN",
    "US_HAWAII",
    "US_MOUNTAIN",
    "US_PACIFIC",
    "US_SAMOA",
    "UTC",
]


# --- restJson1 ser/de ---
def serialize_json(value: NielsenWatermarkTimezones) -> str:
    return value


def deserialize_json(data: str) -> NielsenWatermarkTimezones:
    return cast(NielsenWatermarkTimezones, data)
