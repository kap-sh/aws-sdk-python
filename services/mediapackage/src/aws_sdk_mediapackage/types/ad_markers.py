"""Generated from Smithy shape ``com.amazonaws.mediapackage#AdMarkers``."""

from typing import Literal, TypeAlias, cast

AdMarkers: TypeAlias = Literal[
    "NONE",
    "SCTE35_ENHANCED",
    "PASSTHROUGH",
    "DATERANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdMarkers) -> str:
    return value


def deserialize_json(data: str) -> AdMarkers:
    return cast(AdMarkers, data)
