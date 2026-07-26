"""Generated from Smithy shape ``com.amazonaws.dlm#ScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dlm.types.schedule

ScheduleList: TypeAlias = list["capo_dlm.types.schedule.Schedule"]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleList) -> list:
    import capo_dlm.types.schedule

    out: list = []
    for item in value:
        out.append(capo_dlm.types.schedule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScheduleList:
    import capo_dlm.types.schedule

    out: ScheduleList = []
    for item in data:
        out.append(capo_dlm.types.schedule.deserialize_json(item))
    return out
