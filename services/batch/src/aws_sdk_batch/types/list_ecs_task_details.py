"""Generated from Smithy shape ``com.amazonaws.batch#ListEcsTaskDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.ecs_task_details

ListEcsTaskDetails: TypeAlias = list[
    "aws_sdk_batch.types.ecs_task_details.EcsTaskDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEcsTaskDetails) -> list:
    import aws_sdk_batch.types.ecs_task_details

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.ecs_task_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListEcsTaskDetails:
    import aws_sdk_batch.types.ecs_task_details

    out: ListEcsTaskDetails = []
    for item in data:
        out.append(aws_sdk_batch.types.ecs_task_details.deserialize_json(item))
    return out
