"""Generated from Smithy shape ``com.amazonaws.odb#DaysOfWeek``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.day_of_week

DaysOfWeek: TypeAlias = list["aws_sdk_odb.types.day_of_week.DayOfWeek"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DaysOfWeek) -> list:
    import aws_sdk_odb.types.day_of_week

    out: list = []
    for item in value:
        out.append(aws_sdk_odb.types.day_of_week.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DaysOfWeek:
    import aws_sdk_odb.types.day_of_week

    out: DaysOfWeek = []
    for item in data:
        out.append(aws_sdk_odb.types.day_of_week.deserialize_aws_json_1_0(item))
    return out
