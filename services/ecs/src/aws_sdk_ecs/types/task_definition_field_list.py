"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition_field

TaskDefinitionFieldList: TypeAlias = list[
    "aws_sdk_ecs.types.task_definition_field.TaskDefinitionField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskDefinitionFieldList) -> list:
    import aws_sdk_ecs.types.task_definition_field

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.task_definition_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskDefinitionFieldList:
    import aws_sdk_ecs.types.task_definition_field

    out: TaskDefinitionFieldList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.task_definition_field.deserialize_aws_json_1_1(item)
        )
    return out
