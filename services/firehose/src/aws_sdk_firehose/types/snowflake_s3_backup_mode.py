"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeS3BackupMode``."""

from typing import Literal, TypeAlias, cast

SnowflakeS3BackupMode: TypeAlias = Literal[
    "FailedDataOnly",
    "AllData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnowflakeS3BackupMode:
    return cast(SnowflakeS3BackupMode, data)
