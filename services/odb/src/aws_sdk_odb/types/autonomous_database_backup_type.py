"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

AutonomousDatabaseBackupType: TypeAlias = Literal[
    "INCREMENTAL",
    "FULL",
    "LONGTERM",
    "VIRTUAL_FULL",
    "CUMULATIVE_INCREMENTAL",
    "ROLL_FORWARD_IMAGE_COPY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREMENTAL",
        "FULL",
        "LONGTERM",
        "VIRTUAL_FULL",
        "CUMULATIVE_INCREMENTAL",
        "ROLL_FORWARD_IMAGE_COPY",
    )
)


def serialize_aws_json_1_0(value: AutonomousDatabaseBackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseBackupType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutonomousDatabaseBackupType value: {data!r}"
        )
    return cast(AutonomousDatabaseBackupType, data)
