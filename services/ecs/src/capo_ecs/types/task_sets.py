"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.task_set

TaskSets: TypeAlias = list["capo_ecs.types.task_set.TaskSet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSets) -> list:
    import capo_ecs.types.task_set

    out: list = []
    for item in value:
        out.append(capo_ecs.types.task_set.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskSets:
    import capo_ecs.types.task_set

    out: TaskSets = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.task_set.deserialize_aws_json_1_1(item))
    return out
