"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesBlockDeviceMapping``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.scheduled_instances_ebs
    import aws_sdk_ec2.types.string


class ScheduledInstancesBlockDeviceMapping(TypedDict):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    ebs: NotRequired["aws_sdk_ec2.types.scheduled_instances_ebs.ScheduledInstancesEbs"]
    """<p>Parameters used to set up EBS volumes automatically when the instance is launched.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string.</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (<code>ephemeral</code>N). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for <code>ephemeral0</code> and <code>ephemeral1</code>. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p> <p>Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.</p>"""
