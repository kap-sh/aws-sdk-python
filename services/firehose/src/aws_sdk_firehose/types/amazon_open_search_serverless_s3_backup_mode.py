"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

AmazonOpenSearchServerlessS3BackupMode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AmazonOpenSearchServerlessS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonOpenSearchServerlessS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmazonOpenSearchServerlessS3BackupMode value: {data!r}"
        )
    return cast(AmazonOpenSearchServerlessS3BackupMode, data)
