"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobStatus``."""

from typing import Literal, TypeAlias, cast

CallAnalyticsJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CallAnalyticsJobStatus:
    return cast(CallAnalyticsJobStatus, data)
