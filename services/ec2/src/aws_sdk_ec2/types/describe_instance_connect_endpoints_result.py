"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceConnectEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_connect_endpoint_set
    import aws_sdk_ec2.types.next_token


class DescribeInstanceConnectEndpointsResult(TypedDict):
    instance_connect_endpoints: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_set.InstanceConnectEndpointSet"
    ]
    """<p>Information about the EC2 Instance Connect Endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
