"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceIamInstanceProfileAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association


class ReplaceIamInstanceProfileAssociationResult(TypedDict):
    iam_instance_profile_association: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association.IamInstanceProfileAssociation"
    ]
    """<p>Information about the IAM instance profile association.</p>"""
