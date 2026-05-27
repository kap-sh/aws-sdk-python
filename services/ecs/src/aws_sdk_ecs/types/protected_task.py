"""Generated from Smithy shape ``com.amazonaws.ecs#ProtectedTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ProtectedTask(TypedDict):
    task_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task ARN.</p>"""
    protection_enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>The protection status of the task. If scale-in protection is on for a task, the value is <code>true</code>. Otherwise, it is <code>false</code>.</p>"""
    expiration_date: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The epoch time when protection for the task will expire.</p>"""
