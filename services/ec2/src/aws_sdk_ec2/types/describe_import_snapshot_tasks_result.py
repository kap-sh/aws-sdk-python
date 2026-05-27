"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImportSnapshotTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_snapshot_task_list
    import aws_sdk_ec2.types.string


class DescribeImportSnapshotTasksResult(TypedDict):
    import_snapshot_tasks: NotRequired[
        "aws_sdk_ec2.types.import_snapshot_task_list.ImportSnapshotTaskList"
    ]
    """<p>A list of zero or more import snapshot tasks that are currently active or were completed or canceled in the previous 7 days.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to get the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
