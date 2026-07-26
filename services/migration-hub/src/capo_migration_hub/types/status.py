"""Generated from Smithy shape ``com.amazonaws.migrationhub#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    return cast(Status, data)
