"""Generated from Smithy shape ``com.amazonaws.batch#TaskContainerDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.task_container_dependency

TaskContainerDependencyList: TypeAlias = list[
    "capo_batch.types.task_container_dependency.TaskContainerDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskContainerDependencyList) -> list:
    import capo_batch.types.task_container_dependency

    out: list = []
    for item in value:
        out.append(capo_batch.types.task_container_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaskContainerDependencyList:
    import capo_batch.types.task_container_dependency

    out: TaskContainerDependencyList = []
    for item in data:
        out.append(capo_batch.types.task_container_dependency.deserialize_json(item))
    return out
