"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsSkippedReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

CallAnalyticsSkippedReasonCode: TypeAlias = Literal[
    "INSUFFICIENT_CONVERSATION_CONTENT",
    "FAILED_SAFETY_GUIDELINES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSUFFICIENT_CONVERSATION_CONTENT",
        "FAILED_SAFETY_GUIDELINES",
    )
)


def serialize_aws_json_1_1(value: CallAnalyticsSkippedReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsSkippedReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CallAnalyticsSkippedReasonCode value: {data!r}"
        )
    return cast(CallAnalyticsSkippedReasonCode, data)
