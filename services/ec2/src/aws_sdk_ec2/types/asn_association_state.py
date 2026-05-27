"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociationState``."""

from typing import Literal, TypeAlias

AsnAssociationState: TypeAlias = Literal[
    "disassociated",
    "failed-disassociation",
    "failed-association",
    "pending-disassociation",
    "pending-association",
    "associated",
]
