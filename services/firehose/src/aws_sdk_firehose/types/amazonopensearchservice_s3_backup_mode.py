"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceS3BackupMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

AmazonopensearchserviceS3BackupMode: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AmazonopensearchserviceS3BackupMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonopensearchserviceS3BackupMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmazonopensearchserviceS3BackupMode value: {data!r}"
        )
    return cast(AmazonopensearchserviceS3BackupMode, data)
