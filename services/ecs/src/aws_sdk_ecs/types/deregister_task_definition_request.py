"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterTaskDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeregisterTaskDefinitionRequest(TypedDict):
    task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full Amazon Resource Name (ARN) of the task definition to deregister. You must specify a <code>revision</code>.</p>"""
