"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskContainerProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.task_container_properties

ListTaskContainerProperties: TypeAlias = list[
    "aws_sdk_batch.types.task_container_properties.TaskContainerProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskContainerProperties) -> list:
    import aws_sdk_batch.types.task_container_properties

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.task_container_properties.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskContainerProperties:
    import aws_sdk_batch.types.task_container_properties

    out: ListTaskContainerProperties = []
    for item in data:
        out.append(aws_sdk_batch.types.task_container_properties.deserialize_json(item))
    return out
