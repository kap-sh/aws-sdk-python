"""Generated from Smithy shape ``com.amazonaws.ec2#UserIdGroupPair``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UserIdGroupPair(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the security group rule that references this user ID group pair.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=;{}!$*</p>"""
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an Amazon Web Services account.</p> <p>For a referenced security group in another VPC, the account ID of the referenced security group is returned in the response. If the referenced security group is deleted, this value is not returned.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Default VPC] The name of the security group. For a security group in a nondefault VPC, use the security group ID. </p> <p>For a referenced security group in another VPC, this value is not returned if the referenced security group is deleted.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the referenced security group, if applicable.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection, if applicable.</p>"""
    peering_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of a VPC peering connection, if applicable.</p>"""
