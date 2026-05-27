"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterTaskDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.task_definition


class RegisterTaskDefinitionResponse(TypedDict):
    task_definition: NotRequired["aws_sdk_ecs.types.task_definition.TaskDefinition"]
    """<p>The full description of the registered task definition.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The list of tags associated with the task definition.</p>"""
