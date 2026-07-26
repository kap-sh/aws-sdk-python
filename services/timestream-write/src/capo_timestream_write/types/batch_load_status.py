"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadStatus``."""

from typing import Literal, TypeAlias, cast

BatchLoadStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "PROGRESS_STOPPED",
    "PENDING_RESUME",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchLoadStatus:
    return cast(BatchLoadStatus, data)
