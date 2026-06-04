"""Generated from Smithy shape ``com.amazonaws.ecs#TaskFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_field

TaskFieldList: TypeAlias = list["aws_sdk_ecs.types.task_field.TaskField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFieldList) -> list:
    import aws_sdk_ecs.types.task_field

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.task_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskFieldList:
    import aws_sdk_ecs.types.task_field

    out: TaskFieldList = []
    for item in data:
        out.append(aws_sdk_ecs.types.task_field.deserialize_aws_json_1_1(item))
    return out
