"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
