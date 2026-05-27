"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportImageTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_task_list
    import aws_sdk_ec2.types.string


class DescribeImportImageTasksResult(TypedDict):
    import_image_tasks: NotRequired[
        "aws_sdk_ec2.types.import_image_task_list.ImportImageTaskList"
    ]
    """<p>A list of zero or more import image tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
