"""Generated from Smithy shape ``com.amazonaws.scheduler#ScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.schedule_summary

ScheduleList: TypeAlias = list[
    "aws_sdk_scheduler.types.schedule_summary.ScheduleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleList) -> list:
    import aws_sdk_scheduler.types.schedule_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_scheduler.types.schedule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleList:
    import aws_sdk_scheduler.types.schedule_summary

    out: ScheduleList = []
    for item in data:
        out.append(aws_sdk_scheduler.types.schedule_summary.deserialize_json(item))
    return out
