"""Generated from Smithy shape ``com.amazonaws.glue#JobRunState``."""

from typing import Literal, TypeAlias, cast

JobRunState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
    "ERROR",
    "WAITING",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobRunState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobRunState:
    return cast(JobRunState, data)
