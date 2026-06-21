"""Generated from Smithy shape ``com.amazonaws.firehose#RedshiftS3BackupMode``."""

from typing import Literal, TypeAlias, cast

RedshiftS3BackupMode: TypeAlias = Literal[
    "Disabled",
    "Enabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedshiftS3BackupMode:
    return cast(RedshiftS3BackupMode, data)
