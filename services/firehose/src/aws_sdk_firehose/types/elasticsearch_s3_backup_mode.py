"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ElasticsearchS3BackupMode: TypeAlias = Literal[
    "FailedDocumentsOnly",
    "AllDocuments",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FailedDocumentsOnly",
        "AllDocuments",
    )
)


def serialize_aws_json_1_1(value: ElasticsearchS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ElasticsearchS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ElasticsearchS3BackupMode value: {data!r}")
    return cast(ElasticsearchS3BackupMode, data)
