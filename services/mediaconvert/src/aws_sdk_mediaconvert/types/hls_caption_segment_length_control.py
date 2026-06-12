"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsCaptionSegmentLengthControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Set Caption segment length control to Match video to create caption segments that align with the video segments from the first video output in this output group. For example, if the video segments are 2 seconds long, your WebVTT segments will also be 2 seconds long. Keep the default setting, Large segments to create caption segments that are 300 seconds long."""
HlsCaptionSegmentLengthControl: TypeAlias = Literal[
    "LARGE_SEGMENTS",
    "MATCH_VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LARGE_SEGMENTS",
        "MATCH_VIDEO",
    )
)


def serialize_json(value: HlsCaptionSegmentLengthControl) -> str:
    return value


def deserialize_json(data: str) -> HlsCaptionSegmentLengthControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HlsCaptionSegmentLengthControl value: {data!r}"
        )
    return cast(HlsCaptionSegmentLengthControl, data)
