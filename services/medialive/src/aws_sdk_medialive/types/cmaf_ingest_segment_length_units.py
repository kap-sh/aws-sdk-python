"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestSegmentLengthUnits``."""

from typing import Literal, TypeAlias, cast

"""Cmaf Ingest Segment Length Units"""
CmafIngestSegmentLengthUnits: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestSegmentLengthUnits) -> str:
    return value


def deserialize_json(data: str) -> CmafIngestSegmentLengthUnits:
    return cast(CmafIngestSegmentLengthUnits, data)
