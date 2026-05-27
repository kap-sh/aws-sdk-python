"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.tasks


class DescribeTasksResponse(TypedDict):
    tasks: NotRequired["aws_sdk_ecs.types.tasks.Tasks"]
    """<p>The list of tasks.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
