"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAttachedApplianceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_attached_appliance

NatGatewayAttachedApplianceList: TypeAlias = list[
    "aws_sdk_ec2.types.nat_gateway_attached_appliance.NatGatewayAttachedAppliance"
]
