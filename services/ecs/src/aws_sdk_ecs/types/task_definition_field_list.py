"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition_field

TaskDefinitionFieldList: TypeAlias = list[
    "aws_sdk_ecs.types.task_definition_field.TaskDefinitionField"
]
