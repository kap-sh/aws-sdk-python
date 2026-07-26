"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "COMPLETED",
    "PARTIAL_SUCCESS",
    "FAILED",
    "STOP_REQUESTED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    return cast(JobStatus, data)
