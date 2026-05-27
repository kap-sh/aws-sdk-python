"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedAppliance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_appliance_modify_state
    import aws_sdk_ec2.types.nat_gateway_appliance_state
    import aws_sdk_ec2.types.nat_gateway_appliance_type
    import aws_sdk_ec2.types.string


class NatGatewayAttachedAppliance(TypedDict):
    type: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_type.NatGatewayApplianceType"
    ]
    """<p>The type of appliance attached to the NAT Gateway. For network firewall proxy functionality, this will be \"network-firewall-proxy\".</p>"""
    appliance_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the attached appliance, identifying the specific proxy or security appliance resource.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The VPC endpoint ID used to route traffic from application VPCs to the proxy for inspection and filtering.</p>"""
    attachment_state: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_state.NatGatewayApplianceState"
    ]
    """<p>The current attachment state of the appliance.</p>"""
    modification_state: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_appliance_modify_state.NatGatewayApplianceModifyState"
    ]
    """<p>The current modification state of the appliance.</p>"""
    failure_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The failure code if the appliance attachment or modification operation failed.</p>"""
    failure_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A descriptive message explaining the failure if the appliance attachment or modification operation failed.</p>"""
