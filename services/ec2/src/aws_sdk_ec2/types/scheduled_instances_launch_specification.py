"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesLaunchSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.key_pair_name
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set
    import aws_sdk_ec2.types.scheduled_instances_iam_instance_profile
    import aws_sdk_ec2.types.scheduled_instances_monitoring
    import aws_sdk_ec2.types.scheduled_instances_network_interface_set
    import aws_sdk_ec2.types.scheduled_instances_placement
    import aws_sdk_ec2.types.scheduled_instances_security_group_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class ScheduledInstancesLaunchSpecification(TypedDict):
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set.ScheduledInstancesBlockDeviceMappingSet"
    ]
    """<p>The block device mapping entries.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_iam_instance_profile.ScheduledInstancesIamInstanceProfile"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI).</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_monitoring.ScheduledInstancesMonitoring"
    ]
    """<p>Enable or disable monitoring for the instances.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_network_interface_set.ScheduledInstancesNetworkInterfaceSet"
    ]
    """<p>The network interfaces.</p>"""
    placement: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_placement.ScheduledInstancesPlacement"
    ]
    """<p>The placement information.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.scheduled_instances_security_group_id_set.ScheduledInstancesSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to launch the instances.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The base64-encoded MIME user data.</p>"""
