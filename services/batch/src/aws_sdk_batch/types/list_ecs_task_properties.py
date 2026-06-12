"""Generated from Smithy shape ``com.amazonaws.batch#ListEcsTaskProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.ecs_task_properties

ListEcsTaskProperties: TypeAlias = list[
    "aws_sdk_batch.types.ecs_task_properties.EcsTaskProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEcsTaskProperties) -> list:
    import aws_sdk_batch.types.ecs_task_properties

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.ecs_task_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListEcsTaskProperties:
    import aws_sdk_batch.types.ecs_task_properties

    out: ListEcsTaskProperties = []
    for item in data:
        out.append(aws_sdk_batch.types.ecs_task_properties.deserialize_json(item))
    return out
