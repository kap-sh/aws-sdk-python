"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_reference_resource_type
    import aws_sdk_ec2.types.resource_type_option_list


class ResourceTypeRequest(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_reference_resource_type.ImageReferenceResourceType"
    ]
    """<p>The resource type.</p>"""
    resource_type_options: NotRequired[
        "aws_sdk_ec2.types.resource_type_option_list.ResourceTypeOptionList"
    ]
    """<p>The options that affect the scope of the response. Valid only when <code>ResourceType</code> is <code>ec2:Instance</code> or <code>ec2:LaunchTemplate</code>.</p>"""
