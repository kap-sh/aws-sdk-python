"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeExportImageTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_export_image_tasks_max_results
    import aws_sdk_ec2.types.export_image_task_id_list
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeExportImageTasksRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Filter tasks using the <code>task-state</code> filter and one of the following values: <code>active</code>, <code>completed</code>, <code>deleting</code>, or <code>deleted</code>.</p>"""
    export_image_task_ids: NotRequired[
        "aws_sdk_ec2.types.export_image_task_id_list.ExportImageTaskIdList"
    ]
    """<p>The IDs of the export image tasks.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_export_image_tasks_max_results.DescribeExportImageTasksMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>A token that indicates the next page of results.</p>"""
