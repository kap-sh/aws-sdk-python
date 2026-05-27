"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_connection_set


class DescribeVpcEndpointConnectionsResult(TypedDict):
    vpc_endpoint_connections: NotRequired[
        "aws_sdk_ec2.types.vpc_endpoint_connection_set.VpcEndpointConnectionSet"
    ]
    """<p>Information about the VPC endpoint connections.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
