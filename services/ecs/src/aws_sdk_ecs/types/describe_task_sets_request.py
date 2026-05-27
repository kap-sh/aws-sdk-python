"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.task_set_field_list


class DescribeTaskSetsRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task sets exist in.</p>"""
    service: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task sets exist in.</p>"""
    task_sets: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The ID or full Amazon Resource Name (ARN) of task sets to describe.</p>"""
    include: NotRequired["aws_sdk_ecs.types.task_set_field_list.TaskSetFieldList"]
    """<p>Specifies whether to see the resource tags for the task set. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""
