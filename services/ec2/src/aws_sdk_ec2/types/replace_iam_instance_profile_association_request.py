"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceIamInstanceProfileAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_id
    import aws_sdk_ec2.types.iam_instance_profile_specification


class ReplaceIamInstanceProfileAssociationRequest(TypedDict):
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    association_id: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_id.IamInstanceProfileAssociationId"
    ]
    """<p>The ID of the existing IAM instance profile association.</p>"""
