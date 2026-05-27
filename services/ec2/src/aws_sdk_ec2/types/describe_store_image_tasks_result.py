"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStoreImageTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.store_image_task_result_set
    import aws_sdk_ec2.types.string


class DescribeStoreImageTasksResult(TypedDict):
    store_image_task_results: NotRequired[
        "aws_sdk_ec2.types.store_image_task_result_set.StoreImageTaskResultSet"
    ]
    """<p>The information about the AMI store tasks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
