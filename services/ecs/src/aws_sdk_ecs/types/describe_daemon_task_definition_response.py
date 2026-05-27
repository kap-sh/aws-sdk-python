"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition


class DescribeDaemonTaskDefinitionResponse(TypedDict):
    daemon_task_definition: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition.DaemonTaskDefinition"
    ]
    """<p>The full daemon task definition description.</p>"""
