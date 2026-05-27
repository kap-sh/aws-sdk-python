"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListReferenceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference

TransitGatewayPrefixListReferenceSet: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_prefix_list_reference.TransitGatewayPrefixListReference"
]
