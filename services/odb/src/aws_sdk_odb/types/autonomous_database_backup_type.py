"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupType``."""

from typing import Literal, TypeAlias, cast

AutonomousDatabaseBackupType: TypeAlias = Literal[
    "INCREMENTAL",
    "FULL",
    "LONGTERM",
    "VIRTUAL_FULL",
    "CUMULATIVE_INCREMENTAL",
    "ROLL_FORWARD_IMAGE_COPY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseBackupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseBackupType:
    return cast(AutonomousDatabaseBackupType, data)
