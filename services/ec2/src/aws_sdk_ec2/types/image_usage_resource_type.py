"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceType``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_name
    import aws_sdk_ec2.types.image_usage_resource_type_option_list


class ImageUsageResourceType(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_name.ImageUsageResourceTypeName"
    ]
    """<p>The resource type.</p> <p>Valid values: <code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code> </p>"""
    resource_type_options: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_option_list.ImageUsageResourceTypeOptionList"
    ]
    """<p>The options that affect the scope of the report. Valid only when <code>ResourceType</code> is <code>ec2:LaunchTemplate</code>.</p>"""
