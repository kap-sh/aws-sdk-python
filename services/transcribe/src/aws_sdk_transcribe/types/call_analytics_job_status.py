"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

CallAnalyticsJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: CallAnalyticsJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CallAnalyticsJobStatus value: {data!r}")
    return cast(CallAnalyticsJobStatus, data)
