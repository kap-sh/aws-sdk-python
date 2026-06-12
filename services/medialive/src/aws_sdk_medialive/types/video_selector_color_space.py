"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorColorSpace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Video Selector Color Space"""
VideoSelectorColorSpace: TypeAlias = Literal[
    "FOLLOW",
    "HDR10",
    "HLG_2020",
    "REC_601",
    "REC_709",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOW",
        "HDR10",
        "HLG_2020",
        "REC_601",
        "REC_709",
    )
)


def serialize_json(value: VideoSelectorColorSpace) -> str:
    return value


def deserialize_json(data: str) -> VideoSelectorColorSpace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoSelectorColorSpace value: {data!r}")
    return cast(VideoSelectorColorSpace, data)
