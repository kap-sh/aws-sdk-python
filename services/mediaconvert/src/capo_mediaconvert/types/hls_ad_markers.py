"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsAdMarkers``."""

from typing import Literal, TypeAlias, cast

"""Ad marker for Apple HLS manifest."""
HlsAdMarkers: TypeAlias = Literal[
    "ELEMENTAL",
    "ELEMENTAL_SCTE35",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsAdMarkers) -> str:
    return value


def deserialize_json(data: str) -> HlsAdMarkers:
    return cast(HlsAdMarkers, data)
