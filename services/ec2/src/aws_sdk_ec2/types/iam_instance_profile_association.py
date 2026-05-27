"""Generated from Smithy shape ``com.amazonaws.ec2#IamInstanceProfileAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.iam_instance_profile
    import aws_sdk_ec2.types.iam_instance_profile_association_state
    import aws_sdk_ec2.types.string


class IamInstanceProfileAssociation(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile.IamInstanceProfile"
    ]
    """<p>The IAM instance profile.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_state.IamInstanceProfileAssociationState"
    ]
    """<p>The state of the association.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the IAM instance profile was associated with the instance.</p>"""
