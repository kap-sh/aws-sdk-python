"""Generated from Smithy shape ``com.amazonaws.ssm#LastResourceDataSyncStatus``."""

from typing import Literal, TypeAlias, cast

LastResourceDataSyncStatus: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastResourceDataSyncStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastResourceDataSyncStatus:
    return cast(LastResourceDataSyncStatus, data)
