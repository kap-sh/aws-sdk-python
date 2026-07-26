"""Generated from Smithy shape ``com.amazonaws.appflow#SchedulingFrequencyTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.schedule_frequency_type

SchedulingFrequencyTypeList: TypeAlias = list[
    "capo_appflow.types.schedule_frequency_type.ScheduleFrequencyType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulingFrequencyTypeList) -> list:
    import capo_appflow.types.schedule_frequency_type

    out: list = []
    for item in value:
        out.append(capo_appflow.types.schedule_frequency_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchedulingFrequencyTypeList:
    import capo_appflow.types.schedule_frequency_type

    out: SchedulingFrequencyTypeList = []
    for item in data:
        out.append(capo_appflow.types.schedule_frequency_type.deserialize_json(item))
    return out
