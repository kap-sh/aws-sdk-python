"""Generated from Smithy shape ``com.amazonaws.healthlake#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "QUEUED",
    "IN_PROGRESS",
    "COMPLETED_WITH_ERRORS",
    "COMPLETED",
    "FAILED",
    "CANCEL_SUBMITTED",
    "CANCEL_IN_PROGRESS",
    "CANCEL_COMPLETED",
    "CANCEL_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> JobStatus:
    return cast(JobStatus, data)
