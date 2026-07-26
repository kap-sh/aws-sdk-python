"""Generated from Smithy shape ``com.amazonaws.batch#ListEcsTaskDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.ecs_task_details

ListEcsTaskDetails: TypeAlias = list["capo_batch.types.ecs_task_details.EcsTaskDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ListEcsTaskDetails) -> list:
    import capo_batch.types.ecs_task_details

    out: list = []
    for item in value:
        out.append(capo_batch.types.ecs_task_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListEcsTaskDetails:
    import capo_batch.types.ecs_task_details

    out: ListEcsTaskDetails = []
    for item in data:
        out.append(capo_batch.types.ecs_task_details.deserialize_json(item))
    return out
