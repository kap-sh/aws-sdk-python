"""Generated from Smithy shape ``com.amazonaws.batch#ListAttemptTaskContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.attempt_task_container_details

ListAttemptTaskContainerDetails: TypeAlias = list[
    "capo_batch.types.attempt_task_container_details.AttemptTaskContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAttemptTaskContainerDetails) -> list:
    import capo_batch.types.attempt_task_container_details

    out: list = []
    for item in value:
        out.append(capo_batch.types.attempt_task_container_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListAttemptTaskContainerDetails:
    import capo_batch.types.attempt_task_container_details

    out: ListAttemptTaskContainerDetails = []
    for item in data:
        out.append(
            capo_batch.types.attempt_task_container_details.deserialize_json(item)
        )
    return out
