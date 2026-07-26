"""Generated from Smithy shape ``com.amazonaws.firehose#SplunkS3BackupMode``."""

from typing import Literal, TypeAlias, cast

SplunkS3BackupMode: TypeAlias = Literal[
    "FailedEventsOnly",
    "AllEvents",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplunkS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SplunkS3BackupMode:
    return cast(SplunkS3BackupMode, data)
