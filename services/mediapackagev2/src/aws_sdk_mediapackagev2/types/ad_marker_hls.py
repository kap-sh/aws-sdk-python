"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerHls``."""

from typing import Literal, TypeAlias, cast

AdMarkerHls: TypeAlias = Literal[
    "DATERANGE",
    "SCTE35_ENHANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdMarkerHls) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerHls:
    return cast(AdMarkerHls, data)
