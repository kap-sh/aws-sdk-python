"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupSegmentationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Segmentation Mode"""
SmoothGroupSegmentationMode: TypeAlias = Literal[
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


def serialize_json(value: SmoothGroupSegmentationMode) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupSegmentationMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupSegmentationMode value: {data!r}"
        )
    return cast(SmoothGroupSegmentationMode, data)
