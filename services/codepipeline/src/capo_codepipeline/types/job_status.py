"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "Created",
    "Queued",
    "Dispatched",
    "InProgress",
    "TimedOut",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    return cast(JobStatus, data)
