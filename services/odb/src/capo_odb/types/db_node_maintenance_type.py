"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeMaintenanceType``."""

from typing import Literal, TypeAlias, cast

DbNodeMaintenanceType: TypeAlias = Literal["VMDB_REBOOT_MIGRATION",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbNodeMaintenanceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbNodeMaintenanceType:
    return cast(DbNodeMaintenanceType, data)
