"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SegmentationScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Scte35 Segmentation Scope"""
Scte35SegmentationScope: TypeAlias = Literal[
    "ALL_OUTPUT_GROUPS",
    "SCTE35_ENABLED_OUTPUT_GROUPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_OUTPUT_GROUPS",
        "SCTE35_ENABLED_OUTPUT_GROUPS",
    )
)


def serialize_json(value: Scte35SegmentationScope) -> str:
    return value


def deserialize_json(data: str) -> Scte35SegmentationScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte35SegmentationScope value: {data!r}")
    return cast(Scte35SegmentationScope, data)
