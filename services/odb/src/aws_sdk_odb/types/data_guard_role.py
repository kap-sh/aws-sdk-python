"""Generated from Smithy shape ``com.amazonaws.odb#DataGuardRole``."""

from typing import Literal, TypeAlias, cast

DataGuardRole: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
    "DISABLED_STANDBY",
    "BACKUP_COPY",
    "SNAPSHOT_STANDBY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataGuardRole) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataGuardRole:
    return cast(DataGuardRole, data)
