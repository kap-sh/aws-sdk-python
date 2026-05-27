"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTopologyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_set
    import aws_sdk_ec2.types.string


class DescribeInstanceTopologyResult(TypedDict):
    instances: NotRequired["aws_sdk_ec2.types.instance_set.InstanceSet"]
    """<p>Information about the topology of each instance.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
