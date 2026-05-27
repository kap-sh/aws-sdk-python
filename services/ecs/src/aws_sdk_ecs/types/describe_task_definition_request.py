"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.task_definition_field_list


class DescribeTaskDefinitionRequest(TypedDict):
    task_definition: "aws_sdk_ecs.types.string.String"
    """<p>The <code>family</code> for the latest <code>ACTIVE</code> revision, <code>family</code> and <code>revision</code> (<code>family:revision</code>) for a specific revision in the family, or full Amazon Resource Name (ARN) of the task definition to describe.</p>"""
    include: NotRequired[
        "aws_sdk_ecs.types.task_definition_field_list.TaskDefinitionFieldList"
    ]
    """<p>Determines whether to see the resource tags for the task definition. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""
