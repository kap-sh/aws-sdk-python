"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceFamilyCreditSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.unlimited_supported_instance_family


class InstanceFamilyCreditSpecification(TypedDict):
    instance_family: NotRequired[
        "aws_sdk_ec2.types.unlimited_supported_instance_family.UnlimitedSupportedInstanceFamily"
    ]
    """<p>The instance family.</p>"""
    cpu_credits: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The default credit option for CPU usage of the instance family. Valid values are <code>standard</code> and <code>unlimited</code>.</p>"""
