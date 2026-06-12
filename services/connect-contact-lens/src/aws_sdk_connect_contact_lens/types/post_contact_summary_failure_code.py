"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PostContactSummaryFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect_contact_lens.errors import DeserializationError

PostContactSummaryFailureCode: TypeAlias = Literal[
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


def serialize_json(value: PostContactSummaryFailureCode) -> str:
    return value


def deserialize_json(data: str) -> PostContactSummaryFailureCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PostContactSummaryFailureCode value: {data!r}"
        )
    return cast(PostContactSummaryFailureCode, data)
