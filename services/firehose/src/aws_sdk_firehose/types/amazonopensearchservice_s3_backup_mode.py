"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceS3BackupMode``."""

from typing import Literal, TypeAlias, cast

AmazonopensearchserviceS3BackupMode: TypeAlias = Literal[
    "FailedDocumentsOnly",
    "AllDocuments",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonopensearchserviceS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonopensearchserviceS3BackupMode:
    return cast(AmazonopensearchserviceS3BackupMode, data)
