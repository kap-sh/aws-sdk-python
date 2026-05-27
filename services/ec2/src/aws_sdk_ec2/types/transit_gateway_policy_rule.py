"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_rule_meta_data


class TransitGatewayPolicyRule(TypedDict):
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block for the transit gateway policy rule.</p>"""
    source_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The port range for the transit gateway policy rule. Currently this is set to * (all).</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block for the transit gateway policy rule.</p>"""
    destination_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The port range for the transit gateway policy rule. Currently this is set to * (all).</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol used by the transit gateway policy rule.</p>"""
    meta_data: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_rule_meta_data.TransitGatewayPolicyRuleMetaData"
    ]
    """<p>The meta data tags used for the transit gateway policy rule.</p>"""
