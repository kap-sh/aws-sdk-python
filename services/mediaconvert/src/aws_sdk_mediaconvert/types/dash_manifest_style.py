"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashManifestStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how MediaConvert writes SegmentTimeline in your output DASH manifest. To write a SegmentTimeline for outputs that you also specify a Name modifier for: Keep the default value, Basic. Note that if you do not specify a name modifier for an output, MediaConvert will not write a SegmentTimeline for it. To write a common SegmentTimeline in the video AdaptationSet: Choose Compact. Note that MediaConvert will still write a SegmentTimeline in any Representation that does not share a common timeline. To write a video AdaptationSet for each different output framerate, and a common SegmentTimeline in each AdaptationSet: Choose Distinct. To write a SegmentTimeline in each AdaptationSet: Choose Full."""
DashManifestStyle: TypeAlias = Literal[
    "BASIC",
    "COMPACT",
    "DISTINCT",
    "FULL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "COMPACT",
        "DISTINCT",
        "FULL",
    )
)


def serialize_json(value: DashManifestStyle) -> str:
    return value


def deserialize_json(data: str) -> DashManifestStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashManifestStyle value: {data!r}")
    return cast(DashManifestStyle, data)
