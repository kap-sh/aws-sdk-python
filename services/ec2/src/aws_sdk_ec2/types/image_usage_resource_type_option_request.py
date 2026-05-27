"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeOptionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_option_values_list
    import aws_sdk_ec2.types.string


class ImageUsageResourceTypeOptionRequest(TypedDict):
    option_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the option.</p> <p>Valid value: <code>version-depth</code> - The number of launch template versions to check.</p>"""
    option_values: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_option_values_list.ImageUsageResourceTypeOptionValuesList"
    ]
    """<p>A value for the specified option.</p> <p>Valid values: Integers between <code>1</code> and <code>10000</code> </p> <p>Default: <code>20</code> </p>"""
