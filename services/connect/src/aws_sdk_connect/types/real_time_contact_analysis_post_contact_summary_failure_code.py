"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisPostContactSummaryFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RealTimeContactAnalysisPostContactSummaryFailureCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
    "INVALID_ANALYSIS_CONFIGURATION",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUOTA_EXCEEDED",
        "INSUFFICIENT_CONVERSATION_CONTENT",
        "FAILED_SAFETY_GUIDELINES",
        "INVALID_ANALYSIS_CONFIGURATION",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: RealTimeContactAnalysisPostContactSummaryFailureCode) -> str:
    return value


def deserialize_json(data: str) -> RealTimeContactAnalysisPostContactSummaryFailureCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RealTimeContactAnalysisPostContactSummaryFailureCode value: {data!r}"
        )
    return cast(RealTimeContactAnalysisPostContactSummaryFailureCode, data)
