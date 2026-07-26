"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#TaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snow_device_management.types.task_summary

TaskSummaryList: TypeAlias = list[
    "capo_snow_device_management.types.task_summary.TaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSummaryList) -> list:
    import capo_snow_device_management.types.task_summary

    out: list = []
    for item in value:
        out.append(capo_snow_device_management.types.task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskSummaryList:
    import capo_snow_device_management.types.task_summary

    out: TaskSummaryList = []
    for item in data:
        out.append(
            capo_snow_device_management.types.task_summary.deserialize_json(item)
        )
    return out
