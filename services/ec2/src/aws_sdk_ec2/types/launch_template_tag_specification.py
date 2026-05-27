"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateTagSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type
    import aws_sdk_ec2.types.tag_list


class LaunchTemplateTagSpecification(TypedDict):
    resource_type: NotRequired["aws_sdk_ec2.types.resource_type.ResourceType"]
    """<p>The type of resource to tag.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the resource.</p>"""
