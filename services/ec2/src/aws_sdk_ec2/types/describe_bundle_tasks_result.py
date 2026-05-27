"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeBundleTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task_list


class DescribeBundleTasksResult(TypedDict):
    bundle_tasks: NotRequired["aws_sdk_ec2.types.bundle_task_list.BundleTaskList"]
    """<p>Information about the bundle tasks.</p>"""
