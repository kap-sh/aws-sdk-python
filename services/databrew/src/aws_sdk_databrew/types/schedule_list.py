"""Generated from Smithy shape ``com.amazonaws.databrew#ScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_databrew.types.schedule

ScheduleList: TypeAlias = list["aws_sdk_databrew.types.schedule.Schedule"]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleList) -> list:
    import aws_sdk_databrew.types.schedule

    out: list = []
    for item in value:
        out.append(aws_sdk_databrew.types.schedule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleList:
    import aws_sdk_databrew.types.schedule

    out: ScheduleList = []
    for item in data:
        out.append(aws_sdk_databrew.types.schedule.deserialize_json(item))
    return out
