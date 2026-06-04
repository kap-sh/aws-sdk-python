"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSetFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set_field

TaskSetFieldList: TypeAlias = list["aws_sdk_ecs.types.task_set_field.TaskSetField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskSetFieldList) -> list:
    import aws_sdk_ecs.types.task_set_field

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.task_set_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskSetFieldList:
    import aws_sdk_ecs.types.task_set_field

    out: TaskSetFieldList = []
    for item in data:
        out.append(aws_sdk_ecs.types.task_set_field.deserialize_aws_json_1_1(item))
    return out
