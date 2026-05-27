"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCarrierGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway_set
    import aws_sdk_ec2.types.string


class DescribeCarrierGatewaysResult(TypedDict):
    carrier_gateways: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_set.CarrierGatewaySet"
    ]
    """<p>Information about the carrier gateway.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
