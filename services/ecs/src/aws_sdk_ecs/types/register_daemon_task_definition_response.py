"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class RegisterDaemonTaskDefinitionResponse(TypedDict):
    daemon_task_definition_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full Amazon Resource Name (ARN) of the registered daemon task definition.</p>"""
