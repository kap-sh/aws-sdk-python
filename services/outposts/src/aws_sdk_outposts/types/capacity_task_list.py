"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_summary

CapacityTaskList: TypeAlias = list[
    "aws_sdk_outposts.types.capacity_task_summary.CapacityTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskList) -> list:
    import aws_sdk_outposts.types.capacity_task_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.capacity_task_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityTaskList:
    import aws_sdk_outposts.types.capacity_task_summary

    out: CapacityTaskList = []
    for item in data:
        out.append(aws_sdk_outposts.types.capacity_task_summary.deserialize_json(item))
    return out
