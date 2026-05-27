"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_association

TransitGatewayPolicyTableAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_policy_table_association.TransitGatewayPolicyTableAssociation"
]
