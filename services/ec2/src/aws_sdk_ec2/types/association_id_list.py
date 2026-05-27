"""Generated from Smithy shape ``com.amazonaws.ec2#AssociationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_id

AssociationIdList: TypeAlias = list[
    "aws_sdk_ec2.types.iam_instance_profile_association_id.IamInstanceProfileAssociationId"
]
