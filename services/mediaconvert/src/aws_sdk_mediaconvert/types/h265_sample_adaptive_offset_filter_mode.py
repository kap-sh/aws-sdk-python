"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265SampleAdaptiveOffsetFilterMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content"""
H265SampleAdaptiveOffsetFilterMode: TypeAlias = Literal[
    "DEFAULT",
    "ADAPTIVE",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "ADAPTIVE",
        "OFF",
    )
)


def serialize_json(value: H265SampleAdaptiveOffsetFilterMode) -> str:
    return value


def deserialize_json(data: str) -> H265SampleAdaptiveOffsetFilterMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265SampleAdaptiveOffsetFilterMode value: {data!r}"
        )
    return cast(H265SampleAdaptiveOffsetFilterMode, data)
