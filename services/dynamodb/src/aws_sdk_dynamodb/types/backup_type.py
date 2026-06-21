"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupType``."""

from typing import Literal, TypeAlias, cast

BackupType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
    "AWS_BACKUP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupType:
    return cast(BackupType, data)
