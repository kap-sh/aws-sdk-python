"""Generated from Smithy shape ``com.amazonaws.firehose#S3BackupMode``."""

from typing import Literal, TypeAlias, cast

S3BackupMode: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3BackupMode:
    return cast(S3BackupMode, data)
