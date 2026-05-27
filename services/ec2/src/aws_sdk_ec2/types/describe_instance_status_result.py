"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_list
    import aws_sdk_ec2.types.string


class DescribeInstanceStatusResult(TypedDict):
    instance_statuses: NotRequired[
        "aws_sdk_ec2.types.instance_status_list.InstanceStatusList"
    ]
    """<p>Information about the status of the instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
