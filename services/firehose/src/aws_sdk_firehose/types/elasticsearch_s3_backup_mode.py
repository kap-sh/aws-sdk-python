"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchS3BackupMode``."""

from typing import Literal, TypeAlias, cast

ElasticsearchS3BackupMode: TypeAlias = Literal[
    "FailedDocumentsOnly",
    "AllDocuments",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ElasticsearchS3BackupMode:
    return cast(ElasticsearchS3BackupMode, data)
