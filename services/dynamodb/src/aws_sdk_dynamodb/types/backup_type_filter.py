"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupTypeFilter``."""

from typing import Literal, TypeAlias, cast

BackupTypeFilter: TypeAlias = Literal[
    "USER",
    "SYSTEM",
    "AWS_BACKUP",
    "ALL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupTypeFilter) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupTypeFilter:
    return cast(BackupTypeFilter, data)
