"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulitcastDomainAssociationState``."""

from typing import Literal, TypeAlias

TransitGatewayMulitcastDomainAssociationState: TypeAlias = Literal[
    "pendingAcceptance",
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "rejected",
    "failed",
]
