"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMapping``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_instance_block_device
    import aws_sdk_ec2.types.string


class InstanceBlockDeviceMapping(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.ebs_instance_block_device.EbsInstanceBlockDevice"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
