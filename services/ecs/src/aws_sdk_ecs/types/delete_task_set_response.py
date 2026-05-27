"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskSetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class DeleteTaskSetResponse(TypedDict):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>Details about the task set.</p>"""
