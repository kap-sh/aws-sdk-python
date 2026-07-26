"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportStatus``."""

from typing import Literal, TypeAlias, cast

ExportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
