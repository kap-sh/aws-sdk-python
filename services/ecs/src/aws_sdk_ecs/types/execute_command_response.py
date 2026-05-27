"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.session
    import aws_sdk_ecs.types.string


class ExecuteCommandResponse(TypedDict):
    cluster_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    container_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the container.</p>"""
    container_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the container.</p>"""
    interactive: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether the execute command session is running in interactive mode. Amazon ECS only supports initiating interactive sessions, so you must specify <code>true</code> for this value.</p>"""
    session: NotRequired["aws_sdk_ecs.types.session.Session"]
    """<p>The details of the SSM session that was created for this instance of execute-command.</p>"""
    task_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the task.</p>"""
