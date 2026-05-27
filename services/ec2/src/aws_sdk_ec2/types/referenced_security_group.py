"""Generated from Smithy shape ``com.amazonaws.ec2#ReferencedSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ReferencedSecurityGroup(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    peering_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of a VPC peering connection, if applicable.</p>"""
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection (if applicable).</p>"""
