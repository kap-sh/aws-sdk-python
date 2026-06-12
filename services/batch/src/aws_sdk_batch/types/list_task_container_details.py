"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.task_container_details

ListTaskContainerDetails: TypeAlias = list[
    "aws_sdk_batch.types.task_container_details.TaskContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskContainerDetails) -> list:
    import aws_sdk_batch.types.task_container_details

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.task_container_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskContainerDetails:
    import aws_sdk_batch.types.task_container_details

    out: ListTaskContainerDetails = []
    for item in data:
        out.append(aws_sdk_batch.types.task_container_details.deserialize_json(item))
    return out
