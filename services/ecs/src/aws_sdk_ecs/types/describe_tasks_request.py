"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.task_field_list


class DescribeTasksRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task or tasks to describe. If you do not specify a cluster, the default cluster is assumed.</p>"""
    tasks: "aws_sdk_ecs.types.string_list.StringList"
    """<p>A list of up to 100 task IDs or full ARN entries.</p>"""
    include: NotRequired["aws_sdk_ecs.types.task_field_list.TaskFieldList"]
    """<p>Specifies whether you want to see the resource tags for the task. If <code>TAGS</code> is specified, the tags are included in the response. If this field is omitted, tags aren't included in the response.</p>"""
