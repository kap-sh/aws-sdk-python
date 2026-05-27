"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportImageTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_task_list
    import aws_sdk_ec2.types.next_token


class DescribeExportImageTasksResult(TypedDict):
    export_image_tasks: NotRequired[
        "aws_sdk_ec2.types.export_image_task_list.ExportImageTaskList"
    ]
    """<p>Information about the export image tasks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
