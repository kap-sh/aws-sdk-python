"""Generated from Smithy shape ``com.amazonaws.ec2#TagDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type
    import aws_sdk_ec2.types.string


class TagDescription(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The tag key.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.resource_type.ResourceType"]
    """<p>The resource type.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The tag value.</p>"""
