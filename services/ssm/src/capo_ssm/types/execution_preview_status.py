"""Generated from Smithy shape ``com.amazonaws.ssm#ExecutionPreviewStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionPreviewStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionPreviewStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionPreviewStatus:
    return cast(ExecutionPreviewStatus, data)
