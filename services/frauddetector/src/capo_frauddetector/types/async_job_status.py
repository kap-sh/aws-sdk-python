"""Generated from Smithy shape ``com.amazonaws.frauddetector#AsyncJobStatus``."""

from typing import Literal, TypeAlias, cast

AsyncJobStatus: TypeAlias = Literal[
    "IN_PROGRESS_INITIALIZING",
    "IN_PROGRESS",
    "CANCEL_IN_PROGRESS",
    "CANCELED",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AsyncJobStatus:
    return cast(AsyncJobStatus, data)
