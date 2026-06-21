"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupStatus``."""

from typing import Literal, TypeAlias, cast

AutonomousDatabaseBackupStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseBackupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AutonomousDatabaseBackupStatus:
    return cast(AutonomousDatabaseBackupStatus, data)
