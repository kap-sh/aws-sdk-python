"""Generated from Smithy shape ``com.amazonaws.odb#DataGuardRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DataGuardRole: TypeAlias = Literal[
    "PRIMARY",
    "STANDBY",
    "DISABLED_STANDBY",
    "BACKUP_COPY",
    "SNAPSHOT_STANDBY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "STANDBY",
        "DISABLED_STANDBY",
        "BACKUP_COPY",
        "SNAPSHOT_STANDBY",
    )
)


def serialize_aws_json_1_0(value: DataGuardRole) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DataGuardRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataGuardRole value: {data!r}")
    return cast(DataGuardRole, data)
