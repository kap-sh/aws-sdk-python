"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsSegmentationMarkers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Segmentation Markers"""
M2tsSegmentationMarkers: TypeAlias = Literal[
    "EBP",
    "EBP_LEGACY",
    "NONE",
    "PSI_SEGSTART",
    "RAI_ADAPT",
    "RAI_SEGSTART",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBP",
        "EBP_LEGACY",
        "NONE",
        "PSI_SEGSTART",
        "RAI_ADAPT",
        "RAI_SEGSTART",
    )
)


def serialize_json(value: M2tsSegmentationMarkers) -> str:
    return value


def deserialize_json(data: str) -> M2tsSegmentationMarkers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsSegmentationMarkers value: {data!r}")
    return cast(M2tsSegmentationMarkers, data)
