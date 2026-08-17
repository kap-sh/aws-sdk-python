"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSetFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.task_set_field

TaskSetFieldList: TypeAlias = list["capo_ecs.types.task_set_field.TaskSetField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSetFieldList) -> list:
    import capo_ecs.types.task_set_field

    out: list = []
    for item in value:
        out.append(capo_ecs.types.task_set_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskSetFieldList:
    import capo_ecs.types.task_set_field

    out: TaskSetFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.task_set_field.deserialize_aws_json_1_1(item))
    return out
