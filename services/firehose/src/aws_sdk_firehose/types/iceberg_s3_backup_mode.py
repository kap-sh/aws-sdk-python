"""Generated from Smithy shape ``com.amazonaws.firehose#IcebergS3BackupMode``."""

from typing import Literal, TypeAlias, cast

IcebergS3BackupMode: TypeAlias = Literal[
    "FailedDataOnly",
    "AllData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergS3BackupMode:
    return cast(IcebergS3BackupMode, data)
