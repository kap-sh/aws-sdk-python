"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateTagSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type
    import aws_sdk_ec2.types.tag_list


class LaunchTemplateTagSpecificationRequest(TypedDict):
    resource_type: NotRequired["aws_sdk_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource to tag.</p> <p>Valid Values lists all resource types for Amazon EC2 that can be tagged. When you create a launch template, you can specify tags for the following resource types only: <code>instance</code> | <code>volume</code> | <code>network-interface</code> | <code>spot-instances-request</code>. If the instance does not include the resource type that you specify, the instance launch fails. For example, not all instance types include a volume.</p> <p>To tag a resource after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags to apply to the resource.</p>"""
