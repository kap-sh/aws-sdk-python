"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class UpdateTaskSetResponse(TypedDict):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>Details about the task set.</p>"""
