"""Generated from Smithy shape ``com.amazonaws.storagegateway#DaysOfWeek``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.day_of_week

DaysOfWeek: TypeAlias = list["capo_storage_gateway.types.day_of_week.DayOfWeek"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaysOfWeek) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DaysOfWeek:
    return list(data)
