"""Generated from Smithy shape ``com.amazonaws.batch#ListAttemptTaskContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.attempt_task_container_details

ListAttemptTaskContainerDetails: TypeAlias = list[
    "aws_sdk_batch.types.attempt_task_container_details.AttemptTaskContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAttemptTaskContainerDetails) -> list:
    import aws_sdk_batch.types.attempt_task_container_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.attempt_task_container_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListAttemptTaskContainerDetails:
    import aws_sdk_batch.types.attempt_task_container_details

    out: ListAttemptTaskContainerDetails = []
    for item in data:
        out.append(
            aws_sdk_batch.types.attempt_task_container_details.deserialize_json(item)
        )
    return out
