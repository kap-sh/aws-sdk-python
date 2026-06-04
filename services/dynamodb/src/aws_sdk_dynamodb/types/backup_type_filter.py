"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupTypeFilter``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

BackupTypeFilter: TypeAlias = Literal[
    "USER",
    "SYSTEM",
    "AWS_BACKUP",
    "ALL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SYSTEM",
        "AWS_BACKUP",
        "ALL",
    )
)


def serialize_aws_json_1_0(value: BackupTypeFilter) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupTypeFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupTypeFilter value: {data!r}")
    return cast(BackupTypeFilter, data)
