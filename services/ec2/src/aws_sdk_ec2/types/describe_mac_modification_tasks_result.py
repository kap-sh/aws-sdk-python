"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacModificationTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task_list
    import aws_sdk_ec2.types.string


class DescribeMacModificationTasksResult(TypedDict):
    mac_modification_tasks: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task_list.MacModificationTaskList"
    ]
    """<p>Information about the tasks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
