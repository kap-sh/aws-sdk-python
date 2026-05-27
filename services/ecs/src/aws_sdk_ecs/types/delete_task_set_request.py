"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_boolean
    import aws_sdk_ecs.types.string


class DeleteTaskSetRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>"""
    task_set: "aws_sdk_ecs.types.string.String"
    """<p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>"""
    force: NotRequired["aws_sdk_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>"""
