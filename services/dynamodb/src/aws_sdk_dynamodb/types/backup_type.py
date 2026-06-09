"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

BackupType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
    "AWS_BACKUP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SYSTEM",
        "AWS_BACKUP",
    )
)


def serialize_aws_json_1_0(value: BackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupType value: {data!r}")
    return cast(BackupType, data)
