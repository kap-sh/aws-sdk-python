"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupForVpc``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecurityGroupForVpc(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group's description.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group name.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group owner ID.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group ID.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The security group tags.</p>"""
    primary_vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The VPC ID in which the security group was created.</p>"""
