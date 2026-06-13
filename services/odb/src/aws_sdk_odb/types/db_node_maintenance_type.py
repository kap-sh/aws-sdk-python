"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeMaintenanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DbNodeMaintenanceType: TypeAlias = Literal["VMDB_REBOOT_MIGRATION",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("VMDB_REBOOT_MIGRATION",))


def serialize_aws_json_1_0(value: DbNodeMaintenanceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbNodeMaintenanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbNodeMaintenanceType value: {data!r}")
    return cast(DbNodeMaintenanceType, data)
