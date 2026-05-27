"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.task_sets


class DescribeTaskSetsResponse(TypedDict):
    task_sets: NotRequired["aws_sdk_ecs.types.task_sets.TaskSets"]
    """<p>The list of task sets described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
