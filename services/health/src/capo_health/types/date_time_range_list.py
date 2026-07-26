"""Generated from Smithy shape ``com.amazonaws.health#dateTimeRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.date_time_range

dateTimeRangeList: TypeAlias = list["capo_health.types.date_time_range.DateTimeRange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: dateTimeRangeList) -> list:
    import capo_health.types.date_time_range

    out: list = []
    for item in value:
        out.append(capo_health.types.date_time_range.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> dateTimeRangeList:
    import capo_health.types.date_time_range

    out: dateTimeRangeList = []
    for item in data:
        out.append(capo_health.types.date_time_range.deserialize_aws_json_1_1(item))
    return out
