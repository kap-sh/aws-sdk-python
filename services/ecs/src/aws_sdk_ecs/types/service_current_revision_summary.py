"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceCurrentRevisionSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.string


class ServiceCurrentRevisionSummary(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the current service revision.</p>"""
    requested_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of requested tasks in the current service revision</p>"""
    running_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of running tasks of the current service revision</p>"""
    pending_task_count: "aws_sdk_ecs.types.integer.Integer"
    """<p>The number of pending tasks in the current service revision</p>"""
