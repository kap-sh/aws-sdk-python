"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class SecurityGroup(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    ip_permissions_egress: NotRequired[
        "aws_sdk_ec2.types.ip_permission_list.IpPermissionList"
    ]
    """<p>The outbound rules associated with the security group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the security group.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the security group.</p>"""
    security_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the security group.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the security group.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The inbound rules associated with the security group.</p>"""
