"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

AutonomousDatabaseBackupStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "CREATING",
        "UPDATING",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: AutonomousDatabaseBackupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseBackupStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutonomousDatabaseBackupStatus value: {data!r}"
        )
    return cast(AutonomousDatabaseBackupStatus, data)
