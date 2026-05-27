"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociationState``."""

from typing import Literal, TypeAlias

SecurityGroupVpcAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "association-failed",
    "disassociating",
    "disassociated",
    "disassociation-failed",
]
