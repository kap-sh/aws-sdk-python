"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecurityGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CreateSecurityGroupResult(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the security group.</p>"""
    security_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group ARN.</p>"""
