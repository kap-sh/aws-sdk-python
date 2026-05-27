"""Generated from Smithy shape ``com.amazonaws.ecs#TaskDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition

TaskDefinitionList: TypeAlias = list["aws_sdk_ecs.types.task_definition.TaskDefinition"]
