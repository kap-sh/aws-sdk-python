"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteDaemonTaskDefinitionRequest(TypedDict):
    daemon_task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the daemon task definition to delete.</p>"""
