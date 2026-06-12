"""Generated from Smithy shape ``com.amazonaws.medialive#HlsSegmentationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Segmentation Mode"""
HlsSegmentationMode: TypeAlias = Literal[
    "USE_INPUT_SEGMENTATION",
    "USE_SEGMENT_DURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE_INPUT_SEGMENTATION",
        "USE_SEGMENT_DURATION",
    )
)


def serialize_json(value: HlsSegmentationMode) -> str:
    return value


def deserialize_json(data: str) -> HlsSegmentationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsSegmentationMode value: {data!r}")
    return cast(HlsSegmentationMode, data)
