"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonTaskDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DescribeDaemonTaskDefinitionRequest(TypedDict):
    daemon_task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the daemon task definition to describe.</p>"""
