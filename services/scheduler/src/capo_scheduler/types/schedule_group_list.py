"""Generated from Smithy shape ``com.amazonaws.scheduler#ScheduleGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.schedule_group_summary

ScheduleGroupList: TypeAlias = list[
    "capo_scheduler.types.schedule_group_summary.ScheduleGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleGroupList) -> list:
    import capo_scheduler.types.schedule_group_summary

    out: list = []
    for item in value:
        out.append(capo_scheduler.types.schedule_group_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleGroupList:
    import capo_scheduler.types.schedule_group_summary

    out: ScheduleGroupList = []
    for item in data:
        out.append(capo_scheduler.types.schedule_group_summary.deserialize_json(item))
    return out
