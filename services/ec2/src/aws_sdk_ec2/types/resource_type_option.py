"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeOption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_reference_option_name
    import aws_sdk_ec2.types.resource_type_option_values_list


class ResourceTypeOption(TypedDict):
    option_name: NotRequired[
        "aws_sdk_ec2.types.image_reference_option_name.ImageReferenceOptionName"
    ]
    """<p>The name of the option.</p> <ul> <li> <p>For <code>ec2:Instance</code>:</p> <p>Specify <code>state-name</code> - The current state of the EC2 instance.</p> </li> <li> <p>For <code>ec2:LaunchTemplate</code>:</p> <p>Specify <code>version-depth</code> - The number of launch template versions to check, starting from the most recent version.</p> </li> </ul>"""
    option_values: NotRequired[
        "aws_sdk_ec2.types.resource_type_option_values_list.ResourceTypeOptionValuesList"
    ]
    """<p>A value for the specified option.</p> <ul> <li> <p>For <code>state-name</code>:</p> <ul> <li> <p>Valid values: <code>pending</code> | <code>running</code> | <code>shutting-down</code> | <code>terminated</code> | <code>stopping</code> | <code>stopped</code> </p> </li> <li> <p>Default: All states</p> </li> </ul> </li> <li> <p>For <code>version-depth</code>:</p> <ul> <li> <p>Valid values: Integers between <code>1</code> and <code>10000</code> </p> </li> <li> <p>Default: <code>10</code> </p> </li> </ul> </li> </ul>"""
