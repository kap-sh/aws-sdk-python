"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServicePrimaryTaskSetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_set


class UpdateServicePrimaryTaskSetResponse(TypedDict):
    task_set: NotRequired["aws_sdk_ecs.types.task_set.TaskSet"]
    """<p>The details about the task set.</p>"""
