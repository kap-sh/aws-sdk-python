"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessS3BackupMode``."""

from typing import Literal, TypeAlias, cast

AmazonOpenSearchServerlessS3BackupMode: TypeAlias = Literal[
    "FailedDocumentsOnly",
    "AllDocuments",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonOpenSearchServerlessS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonOpenSearchServerlessS3BackupMode:
    return cast(AmazonOpenSearchServerlessS3BackupMode, data)
