"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReplaceRootVolumeTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_root_volume_tasks
    import aws_sdk_ec2.types.string


class DescribeReplaceRootVolumeTasksResult(TypedDict):
    replace_root_volume_tasks: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_tasks.ReplaceRootVolumeTasks"
    ]
    """<p>Information about the root volume replacement task.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
