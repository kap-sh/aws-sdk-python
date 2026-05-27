"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_definition


class DeregisterTaskDefinitionResponse(TypedDict):
    task_definition: NotRequired["aws_sdk_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the deregistered task.</p>"""
