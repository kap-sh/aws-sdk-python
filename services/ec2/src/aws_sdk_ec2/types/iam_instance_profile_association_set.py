"""Generated from Smithy shape ``com.amazonaws.ec2#IamInstanceProfileAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association

IamInstanceProfileAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.iam_instance_profile_association.IamInstanceProfileAssociation"
]
