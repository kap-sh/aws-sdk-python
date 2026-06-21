"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PostContactSummaryFailureCode``."""

from typing import Literal, TypeAlias, cast

PostContactSummaryFailureCode: TypeAlias = Literal[
    "QUOTA_EXCEEDED",
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
    "INVALID_ANALYSIS_CONFIGURATION",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostContactSummaryFailureCode) -> str:
    return value


def deserialize_json(data: str) -> PostContactSummaryFailureCode:
    return cast(PostContactSummaryFailureCode, data)
