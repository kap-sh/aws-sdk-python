"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_association

TransitGatewayMulticastDomainAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_multicast_domain_association.TransitGatewayMulticastDomainAssociation"
]
