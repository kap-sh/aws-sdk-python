"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition

TaskDefinitionList: TypeAlias = list["aws_sdk_ecs.types.task_definition.TaskDefinition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionList) -> list:
    import aws_sdk_ecs.types.task_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.task_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskDefinitionList:
    import aws_sdk_ecs.types.task_definition

    out: TaskDefinitionList = []
    for item in data:
        out.append(aws_sdk_ecs.types.task_definition.deserialize_aws_json_1_1(item))
    return out
