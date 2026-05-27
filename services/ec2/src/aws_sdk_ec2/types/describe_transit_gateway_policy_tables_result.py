"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayPolicyTablesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_table_list


class DescribeTransitGatewayPolicyTablesResult(TypedDict):
    transit_gateway_policy_tables: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_list.TransitGatewayPolicyTableList"
    ]
    """<p>Describes the transit gateway policy tables.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
