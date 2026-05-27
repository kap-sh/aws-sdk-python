"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotLaunchSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.iam_instance_profile_specification
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_network_interface_specification_list
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.kernel_id
    import aws_sdk_ec2.types.key_pair_name_with_resolver
    import aws_sdk_ec2.types.ramdisk_id
    import aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list
    import aws_sdk_ec2.types.request_spot_launch_specification_security_group_list
    import aws_sdk_ec2.types.run_instances_monitoring_enabled
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.spot_placement
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class RequestSpotLaunchSpecification(TypedDict):
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list.RequestSpotLaunchSpecificationSecurityGroupIdList"
    ]
    """<p>The IDs of the security groups.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.request_spot_launch_specification_security_group_list.RequestSpotLaunchSpecificationSecurityGroupList"
    ]
    """<p>Not supported.</p>"""
    addressing_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>The block device mapping entries. You can't specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instance is optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. Only one instance type can be specified.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired[
        "aws_sdk_ec2.types.key_pair_name_with_resolver.KeyPairNameWithResolver"
    ]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]
    """<p>Indicates whether basic or detailed monitoring is enabled for the instance.</p> <p>Default: Disabled</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface.</p>"""
    placement: NotRequired["aws_sdk_ec2.types.spot_placement.SpotPlacement"]
    """<p>The placement information for the instance.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to launch the instance.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.</p>"""
