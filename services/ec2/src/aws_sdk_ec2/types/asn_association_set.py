"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association

AsnAssociationSet: TypeAlias = list["aws_sdk_ec2.types.asn_association.AsnAssociation"]
