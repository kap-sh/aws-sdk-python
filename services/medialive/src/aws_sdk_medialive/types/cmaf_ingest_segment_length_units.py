"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestSegmentLengthUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf Ingest Segment Length Units"""
CmafIngestSegmentLengthUnits: TypeAlias = Literal[
    "MILLISECONDS",
    "SECONDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MILLISECONDS",
        "SECONDS",
    )
)


def serialize_json(value: CmafIngestSegmentLengthUnits) -> str:
    return value


def deserialize_json(data: str) -> CmafIngestSegmentLengthUnits:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CmafIngestSegmentLengthUnits value: {data!r}"
        )
    return cast(CmafIngestSegmentLengthUnits, data)
