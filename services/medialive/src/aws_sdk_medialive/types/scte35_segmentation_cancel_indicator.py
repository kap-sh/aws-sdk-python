"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SegmentationCancelIndicator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Corresponds to SCTE-35 segmentation_event_cancel_indicator. SEGMENTATION_EVENT_NOT_CANCELED corresponds to 0 in the SCTE-35 specification and indicates that this is an insertion request. SEGMENTATION_EVENT_CANCELED corresponds to 1 in the SCTE-35 specification and indicates that this is a cancelation request, in which case complete this field and the existing event ID to cancel."""
Scte35SegmentationCancelIndicator: TypeAlias = Literal[
    "SEGMENTATION_EVENT_NOT_CANCELED",
    "SEGMENTATION_EVENT_CANCELED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEGMENTATION_EVENT_NOT_CANCELED",
        "SEGMENTATION_EVENT_CANCELED",
    )
)


def serialize_json(value: Scte35SegmentationCancelIndicator) -> str:
    return value


def deserialize_json(data: str) -> Scte35SegmentationCancelIndicator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown Scte35SegmentationCancelIndicator value: {data!r}"
        )
    return cast(Scte35SegmentationCancelIndicator, data)
