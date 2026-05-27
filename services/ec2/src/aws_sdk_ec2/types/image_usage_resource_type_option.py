"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_option_values_list
    import aws_sdk_ec2.types.string


class ImageUsageResourceTypeOption(TypedDict):
    option_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the option.</p>"""
    option_values: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_option_values_list.ImageUsageResourceTypeOptionValuesList"
    ]
    """<p>The number of launch template versions to check.</p>"""
