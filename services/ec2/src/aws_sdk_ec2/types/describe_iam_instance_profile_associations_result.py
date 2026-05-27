"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.iam_instance_profile_association_set
    import aws_sdk_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsResult(TypedDict):
    iam_instance_profile_associations: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_association_set.IamInstanceProfileAssociationSet"
    ]
    """<p>Information about the IAM instance profile associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
