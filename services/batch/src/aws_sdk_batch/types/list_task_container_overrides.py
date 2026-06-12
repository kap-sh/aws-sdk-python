"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskContainerOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.task_container_overrides

ListTaskContainerOverrides: TypeAlias = list[
    "aws_sdk_batch.types.task_container_overrides.TaskContainerOverrides"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskContainerOverrides) -> list:
    import aws_sdk_batch.types.task_container_overrides

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.task_container_overrides.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskContainerOverrides:
    import aws_sdk_batch.types.task_container_overrides

    out: ListTaskContainerOverrides = []
    for item in data:
        out.append(aws_sdk_batch.types.task_container_overrides.deserialize_json(item))
    return out
