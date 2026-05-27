"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServicePrimaryTaskSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UpdateServicePrimaryTaskSetRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>"""
    primary_task_set: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>"""
