"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeEgressOnlyInternetGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway_list
    import aws_sdk_ec2.types.string


class DescribeEgressOnlyInternetGatewaysResult(TypedDict):
    egress_only_internet_gateways: NotRequired[
        "aws_sdk_ec2.types.egress_only_internet_gateway_list.EgressOnlyInternetGatewayList"
    ]
    """<p>Information about the egress-only internet gateways.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
