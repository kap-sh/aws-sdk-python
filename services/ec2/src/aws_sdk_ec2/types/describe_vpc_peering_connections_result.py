"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcPeeringConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_peering_connection_list


class DescribeVpcPeeringConnectionsResult(TypedDict):
    vpc_peering_connections: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_list.VpcPeeringConnectionList"
    ]
    """<p>Information about the VPC peering connections.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
