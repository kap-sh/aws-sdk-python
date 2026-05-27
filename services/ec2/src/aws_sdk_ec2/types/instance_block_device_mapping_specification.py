"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMappingSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_instance_block_device_specification
    import aws_sdk_ec2.types.string


class InstanceBlockDeviceMappingSpecification(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name. For available device names, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html\">Device names for volumes</a>.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.ebs_instance_block_device_specification.EbsInstanceBlockDeviceSpecification"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Suppresses the specified device included in the block device mapping.</p>"""
