"""Generated from Smithy shape ``com.amazonaws.ecs#StopTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class StopTaskRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task to stop. If you do not specify a cluster, the default cluster is assumed.</p>"""
    task: "aws_sdk_ecs.types.string.String"
    """<p>Thefull Amazon Resource Name (ARN) of the task.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An optional message specified when a task is stopped. For example, if you're using a custom scheduler, you can use this parameter to specify the reason for stopping the task here, and the message appears in subsequent <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html\">DescribeTasks</a>&gt; API operations on this task.</p>"""
