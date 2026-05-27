"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayMeteringPoliciesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_metering_policy_list


class DescribeTransitGatewayMeteringPoliciesResult(TypedDict):
    transit_gateway_metering_policies: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_list.TransitGatewayMeteringPolicyList"
    ]
    """<p>Information about the transit gateway metering policies.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
