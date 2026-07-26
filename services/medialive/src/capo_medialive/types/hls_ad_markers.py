"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAdMarkers``."""

from typing import Literal, TypeAlias, cast

"""Hls Ad Markers"""
HlsAdMarkers: TypeAlias = Literal[
    "ADOBE",
    "ELEMENTAL",
    "ELEMENTAL_SCTE35",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> HlsAdMarkers:
    return cast(HlsAdMarkers, data)
