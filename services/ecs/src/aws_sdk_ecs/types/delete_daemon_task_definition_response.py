"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteDaemonTaskDefinitionResponse(TypedDict):
    daemon_task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the deleted daemon task definition.</p>"""
