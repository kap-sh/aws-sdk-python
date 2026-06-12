"""Generated from Smithy shape ``com.amazonaws.backupgateway#DaysOfWeek``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.day_of_week

DaysOfWeek: TypeAlias = list["aws_sdk_backup_gateway.types.day_of_week.DayOfWeek"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DaysOfWeek) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DaysOfWeek:
    return list(data)
