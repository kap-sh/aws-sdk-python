"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPostContactSummaryFailureCode``."""

from typing import Literal, TypeAlias, cast

RealTimeContactAnalysisPostContactSummaryFailureCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
    "INVALID_ANALYSIS_CONFIGURATION",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisPostContactSummaryFailureCode) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisPostContactSummaryFailureCode:
    return cast(RealTimeContactAnalysisPostContactSummaryFailureCode, data)
