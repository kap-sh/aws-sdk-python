"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_endpoint_set


class DescribeVpcEndpointsResult(TypedDict):
    vpc_endpoints: NotRequired["aws_sdk_ec2.types.vpc_endpoint_set.VpcEndpointSet"]
    """<p>Information about the VPC endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""
