"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetLaunchSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.group_identifier_list
    import aws_sdk_ec2.types.iam_instance_profile_specification
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.instance_network_interface_specification_list
    import aws_sdk_ec2.types.instance_requirements
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.key_pair_name
    import aws_sdk_ec2.types.sensitive_user_data
    import aws_sdk_ec2.types.spot_fleet_monitoring
    import aws_sdk_ec2.types.spot_fleet_tag_specification_list
    import aws_sdk_ec2.types.spot_placement
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class SpotFleetLaunchSpecification(TypedDict):
    addressing_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>One or more block devices that are mapped to the Spot Instances. You can't specify both a snapshot ID and an encryption value. This is because only blank volumes can be encrypted on creation. If a snapshot is the basis for a volume, it is not blank and its encryption status is used for the volume encryption status.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS Optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_ec2.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["aws_sdk_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_monitoring.SpotFleetMonitoring"
    ]
    """<p>Enable or disable monitoring for the instances.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_ec2.types.instance_network_interface_specification_list.InstanceNetworkInterfaceSpecificationList"
    ]
    """<p>The network interfaces.</p> <note> <p> <code>SpotFleetLaunchSpecification</code> does not support Elastic Fabric Adapter (EFA). You must use <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateConfig.html\">LaunchTemplateConfig</a> instead.</p> </note>"""
    placement: NotRequired["aws_sdk_ec2.types.spot_placement.SpotPlacement"]
    """<p>The placement information.</p>"""
    ramdisk_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the RAM disk. Some kernels require additional drivers at launch. Check the kernel requirements for information about whether you need to specify a RAM disk. To find kernel requirements, refer to the Amazon Web Services Resource Center and search for the kernel ID.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The IDs of the subnets in which to launch the instances. To specify multiple subnets, separate them using commas; for example, \"subnet-1234abcdeexample1, subnet-0987cdef6example2\".</p> <p>If you specify a network interface, you must specify any subnets as part of the network interface instead of using this parameter.</p>"""
    user_data: NotRequired["aws_sdk_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>The base64-encoded user data that instances use when starting up. User data is limited to 16 KB.</p>"""
    weighted_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.</p> <p>If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.</p> <note> <p>When specifying weights, the price used in the <code>lowestPrice</code> and <code>priceCapacityOptimized</code> allocation strategies is per <i>unit</i> hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested <code>TargetCapacity</code>, resulting in only 1 instance being launched, the price used is per <i>instance</i> hour.</p> </note>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_tag_specification_list.SpotFleetTagSpecificationList"
    ]
    """<p>The tags to apply during creation.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.group_identifier_list.GroupIdentifierList"
    ]
    """<p>The security groups.</p> <p>If you specify a network interface, you must specify any security groups as part of the network interface instead of using this parameter.</p>"""
