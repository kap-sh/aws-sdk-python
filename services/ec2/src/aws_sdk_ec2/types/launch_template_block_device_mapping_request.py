"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_ebs_block_device_request
    import aws_sdk_ec2.types.string


class LaunchTemplateBlockDeviceMappingRequest(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name (for example, /dev/sdh or xvdh).</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.launch_template_ebs_block_device_request.LaunchTemplateEbsBlockDeviceRequest"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string.</p>"""
