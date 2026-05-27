"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_association

PrefixListAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.prefix_list_association.PrefixListAssociation"
]
