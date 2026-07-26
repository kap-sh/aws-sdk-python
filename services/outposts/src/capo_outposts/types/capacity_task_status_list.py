"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.capacity_task_status

CapacityTaskStatusList: TypeAlias = list[
    "capo_outposts.types.capacity_task_status.CapacityTaskStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskStatusList) -> list:
    import capo_outposts.types.capacity_task_status

    out: list = []
    for item in value:
        out.append(capo_outposts.types.capacity_task_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityTaskStatusList:
    import capo_outposts.types.capacity_task_status

    out: CapacityTaskStatusList = []
    for item in data:
        out.append(capo_outposts.types.capacity_task_status.deserialize_json(item))
    return out
