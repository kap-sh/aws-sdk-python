"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

BackupStatus: TypeAlias = Literal[
    "CREATING",
    "DELETED",
    "AVAILABLE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETED",
        "AVAILABLE",
    )
)


def serialize_aws_json_1_0(value: BackupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BackupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupStatus value: {data!r}")
    return cast(BackupStatus, data)
