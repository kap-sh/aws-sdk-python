"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedRolesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_role

AssociatedRolesList: TypeAlias = list[
    "aws_sdk_ec2.types.associated_role.AssociatedRole"
]
