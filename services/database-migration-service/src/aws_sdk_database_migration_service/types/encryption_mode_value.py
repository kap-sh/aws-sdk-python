"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EncryptionModeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

EncryptionModeValue: TypeAlias = Literal[
    "sse-s3",
    "sse-kms",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sse-s3",
        "sse-kms",
    )
)


def serialize_aws_json_1_1(value: EncryptionModeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionModeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionModeValue value: {data!r}")
    return cast(EncryptionModeValue, data)
