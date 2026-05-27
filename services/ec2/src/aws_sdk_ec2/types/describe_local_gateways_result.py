"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewaysResult(TypedDict):
    local_gateways: NotRequired["aws_sdk_ec2.types.local_gateway_set.LocalGatewaySet"]
    """<p>Information about the local gateways.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
