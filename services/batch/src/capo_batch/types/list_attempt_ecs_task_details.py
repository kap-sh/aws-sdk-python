"""Generated from Smithy shape ``com.amazonaws.batch#ListAttemptEcsTaskDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.attempt_ecs_task_details

ListAttemptEcsTaskDetails: TypeAlias = list[
    "capo_batch.types.attempt_ecs_task_details.AttemptEcsTaskDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAttemptEcsTaskDetails) -> list:
    import capo_batch.types.attempt_ecs_task_details

    out: list = []
    for item in value:
        out.append(capo_batch.types.attempt_ecs_task_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListAttemptEcsTaskDetails:
    import capo_batch.types.attempt_ecs_task_details

    out: ListAttemptEcsTaskDetails = []
    for item in data:
        out.append(capo_batch.types.attempt_ecs_task_details.deserialize_json(item))
    return out
