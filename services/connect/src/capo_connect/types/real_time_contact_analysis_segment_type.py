"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentType``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisSegmentType: TypeAlias = Literal[
    "Transcript",
    "Categories",
    "Issues",
    "Event",
    "Attachments",
    "PostContactSummary",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentType) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisSegmentType:
    return cast(RealTimeContactAnalysisSegmentType, data)
