"""Generated from Smithy shape ``com.amazonaws.batch#ListTaskContainerOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.task_container_overrides

ListTaskContainerOverrides: TypeAlias = list[
    "capo_batch.types.task_container_overrides.TaskContainerOverrides"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListTaskContainerOverrides) -> list:
    import capo_batch.types.task_container_overrides

    out: list = []
    for item in value:
        out.append(capo_batch.types.task_container_overrides.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListTaskContainerOverrides:
    import capo_batch.types.task_container_overrides

    out: ListTaskContainerOverrides = []
    for item in data:
        out.append(capo_batch.types.task_container_overrides.deserialize_json(item))
    return out
