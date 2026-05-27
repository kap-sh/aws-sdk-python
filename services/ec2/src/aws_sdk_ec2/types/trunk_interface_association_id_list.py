"""Generated from Smithy shape ``com.amazonaws.ec2#TrunkInterfaceAssociationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.trunk_interface_association_id

TrunkInterfaceAssociationIdList: TypeAlias = list[
    "aws_sdk_ec2.types.trunk_interface_association_id.TrunkInterfaceAssociationId"
]
