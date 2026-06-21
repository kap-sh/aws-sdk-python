"""Generated from Smithy shape ``com.amazonaws.iotwireless#SupportedRfRegion``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported RfRegions</p>"""
SupportedRfRegion: TypeAlias = Literal[
    "EU868",
    "US915",
    "AU915",
    "AS923-1",
    "AS923-2",
    "AS923-3",
    "AS923-4",
    "EU433",
    "CN470",
    "CN779",
    "RU864",
    "KR920",
    "IN865",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedRfRegion) -> str:
    return value


def deserialize_json(data: str) -> SupportedRfRegion:
    return cast(SupportedRfRegion, data)
