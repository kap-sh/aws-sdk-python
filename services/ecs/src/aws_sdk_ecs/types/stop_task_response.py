"""Generated from Smithy shape ``com.amazonaws.ecs#StopTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task


class StopTaskResponse(TypedDict):
    task: NotRequired["aws_sdk_ecs.types.task.Task"]
    """<p>The task that was stopped.</p>"""
