"""Generated from Smithy shape ``com.amazonaws.ecs#TaskSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set

TaskSets: TypeAlias = list["aws_sdk_ecs.types.task_set.TaskSet"]
