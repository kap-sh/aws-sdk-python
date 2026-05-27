"""Generated from Smithy shape ``com.amazonaws.ec2#TrunkInterfaceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.trunk_interface_association

TrunkInterfaceAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.trunk_interface_association.TrunkInterfaceAssociation"
]
