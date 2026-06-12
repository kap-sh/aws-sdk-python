"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisSegmentType: TypeAlias = Literal[
    "Transcript",
    "Categories",
    "Issues",
    "Event",
    "Attachments",
    "PostContactSummary",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Transcript",
        "Categories",
        "Issues",
        "Event",
        "Attachments",
        "PostContactSummary",
    )
)


def serialize_json(value: RealTimeContactAnalysisSegmentType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSegmentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisSegmentType value: {data!r}"
        )
    return cast(RealTimeContactAnalysisSegmentType, data)
