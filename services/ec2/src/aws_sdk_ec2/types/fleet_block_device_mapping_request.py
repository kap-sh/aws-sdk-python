"""Generated from Smithy shape ``com.amazonaws.ec2#FleetBlockDeviceMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_ebs_block_device_request
    import aws_sdk_ec2.types.string


class FleetBlockDeviceMappingRequest(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (<code>ephemeralN</code>). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for <code>ephemeral0</code> and <code>ephemeral1</code>. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p> <p>NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.</p> <p>Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.fleet_ebs_block_device_request.FleetEbsBlockDeviceRequest"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.</p>"""
