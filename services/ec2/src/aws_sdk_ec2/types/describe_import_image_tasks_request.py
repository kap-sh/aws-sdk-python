"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportImageTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.import_task_id_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeImportImageTasksRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Filter tasks using the <code>task-state</code> filter and one of the following values: <code>active</code>, <code>completed</code>, <code>deleting</code>, or <code>deleted</code>.</p>"""
    import_task_ids: NotRequired[
        "aws_sdk_ec2.types.import_task_id_list.ImportTaskIdList"
    ]
    """<p>The IDs of the import image tasks.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A token that indicates the next page of results.</p>"""
