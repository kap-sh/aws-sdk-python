"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoWriteSegmentTimelineInRepresentation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When you enable Precise segment duration in manifests, your DASH manifest shows precise segment durations. The segment duration information appears inside the SegmentTimeline element, inside SegmentTemplate at the Representation level. When this feature isn't enabled, the segment durations in your DASH manifest are approximate. The segment duration information appears in the duration attribute of the SegmentTemplate element."""
DashIsoWriteSegmentTimelineInRepresentation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DashIsoWriteSegmentTimelineInRepresentation) -> str:
    return value


def deserialize_json(data: str) -> DashIsoWriteSegmentTimelineInRepresentation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DashIsoWriteSegmentTimelineInRepresentation value: {data!r}"
        )
    return cast(DashIsoWriteSegmentTimelineInRepresentation, data)
