"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table

TransitGatewayPolicyTableList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_policy_table.TransitGatewayPolicyTable"
]
