"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "INITIALIZING",
    "IN_PROGRESS",
    "FAILED",
    "STOPPED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
