"""Generated from Smithy shape ``com.amazonaws.fsx#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "COMPLETED",
    "UPDATED_OPTIMIZING",
    "OPTIMIZING",
    "PAUSED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    return cast(Status, data)
