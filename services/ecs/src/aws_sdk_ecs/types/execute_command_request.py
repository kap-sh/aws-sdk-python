"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string


class ExecuteCommandRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) or short name of the cluster the task is running in. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container to execute the command on. A container name only needs to be specified for tasks containing multiple containers.</p>"""
    command: "aws_sdk_ecs.types.string.String"
    """<p>The command to run on the container.</p>"""
    interactive: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Use this flag to run your command in interactive mode.</p>"""
    task: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) or ID of the task the container is part of.</p>"""
