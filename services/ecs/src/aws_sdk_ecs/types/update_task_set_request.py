"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.scale
    import aws_sdk_ecs.types.string


class UpdateTaskSetRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>"""
    task_set: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>"""
    scale: "aws_sdk_ecs.types.scale.Scale"
    """<p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>"""
