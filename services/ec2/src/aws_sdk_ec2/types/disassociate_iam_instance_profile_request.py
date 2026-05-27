"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIamInstanceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_id


class DisassociateIamInstanceProfileRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_id.IamInstanceProfileAssociationId"
    ]
    """<p>The ID of the IAM instance profile association.</p>"""
