"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.iam_instance_profile_specification
    import aws_sdk_ec2.types.instance_network_interface_specification_list
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.run_instances_monitoring_enabled
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.spot_placement
    import aws_sdk_ec2.types.string


class LaunchSpecification(TypedDict):
    user_data: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.</p>"""
    addressing_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>The block device mapping entries.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. Only one instance type can be specified.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.spot_placement.SpotPlacement"]
    """<p>The placement information for the instance.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the RAM disk.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet in which to launch the instance.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>The IDs of the security groups.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]
