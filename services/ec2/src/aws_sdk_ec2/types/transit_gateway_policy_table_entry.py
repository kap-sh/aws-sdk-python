"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_rule
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class TransitGatewayPolicyTableEntry(TypedDict):
    policy_rule_number: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule number for the transit gateway policy table entry.</p>"""
    policy_rule: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_rule.TransitGatewayPolicyRule"
    ]
    """<p>The policy rule associated with the transit gateway policy table.</p>"""
    target_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the target route table.</p>"""
