"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskContainerDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.task_container_details

ListTaskContainerDetails: TypeAlias = list[
    "capo_batch.types.task_container_details.TaskContainerDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskContainerDetails) -> list:
    import capo_batch.types.task_container_details

    out: list = []
    for item in value:
        out.append(capo_batch.types.task_container_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskContainerDetails:
    import capo_batch.types.task_container_details

    out: ListTaskContainerDetails = []
    for item in data:
        out.append(capo_batch.types.task_container_details.deserialize_json(item))
    return out
