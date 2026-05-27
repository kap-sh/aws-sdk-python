"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMapping``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_ebs_block_device
    import aws_sdk_ec2.types.string


class LaunchTemplateBlockDeviceMapping(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (ephemeralN).</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.launch_template_ebs_block_device.LaunchTemplateEbsBlockDevice"
    ]
    """<p>Information about the block device for an EBS volume.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string.</p>"""
