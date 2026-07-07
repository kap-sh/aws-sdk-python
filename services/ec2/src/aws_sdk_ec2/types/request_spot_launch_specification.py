"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotLaunchSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

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


class RequestSpotLaunchSpecification(TypedDict, closed=True):
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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotLaunchSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_ids" in value:
        import aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list

        aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "security_groups" in value:
        import aws_sdk_ec2.types.request_spot_launch_specification_security_group_list

        aws_sdk_ec2.types.request_spot_launch_specification_security_group_list.serialize_ec2_query(
            value["security_groups"], pairs, f"{prefix}.SecurityGroups"
        )
    if "addressing_type" in value:
        pairs.append((f"{prefix}.AddressingType", str(value["addressing_type"])))
    if "block_device_mappings" in value:
        import aws_sdk_ec2.types.block_device_mapping_list

        aws_sdk_ec2.types.block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{prefix}.BlockDeviceMapping"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import aws_sdk_ec2.types.iam_instance_profile_specification

        aws_sdk_ec2.types.iam_instance_profile_specification.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{prefix}.IamInstanceProfile"
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "kernel_id" in value:
        pairs.append((f"{prefix}.KernelId", str(value["kernel_id"])))
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "monitoring" in value:
        import aws_sdk_ec2.types.run_instances_monitoring_enabled

        aws_sdk_ec2.types.run_instances_monitoring_enabled.serialize_ec2_query(
            value["monitoring"], pairs, f"{prefix}.Monitoring"
        )
    if "network_interfaces" in value:
        import aws_sdk_ec2.types.instance_network_interface_specification_list

        aws_sdk_ec2.types.instance_network_interface_specification_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{prefix}.NetworkInterfaces"
        )
    if "placement" in value:
        import aws_sdk_ec2.types.spot_placement

        aws_sdk_ec2.types.spot_placement.serialize_ec2_query(
            value["placement"], pairs, f"{prefix}.Placement"
        )
    if "ramdisk_id" in value:
        pairs.append((f"{prefix}.RamdiskId", str(value["ramdisk_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "user_data" in value:
        pairs.append((f"{prefix}.UserData", str(value["user_data"])))


def deserialize_ec2_query(el: Element) -> RequestSpotLaunchSpecification:
    out: RequestSpotLaunchSpecification = {}  # type: ignore[typeddict-item]
    if el.find("SecurityGroupIds") is not None:
        import aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_ec2.types.request_spot_launch_specification_security_group_id_list.deserialize_ec2_query(
                el, "SecurityGroupIds"
            )
        )
    if el.find("SecurityGroups") is not None:
        import aws_sdk_ec2.types.request_spot_launch_specification_security_group_list

        out["security_groups"] = (
            aws_sdk_ec2.types.request_spot_launch_specification_security_group_list.deserialize_ec2_query(
                el, "SecurityGroups"
            )
        )
    child_addressing_type = el.find("AddressingType")
    if child_addressing_type is not None:
        out["addressing_type"] = str(child_addressing_type.text or "")
    if el.find("BlockDeviceMapping") is not None:
        import aws_sdk_ec2.types.block_device_mapping_list

        out["block_device_mappings"] = (
            aws_sdk_ec2.types.block_device_mapping_list.deserialize_ec2_query(
                el, "BlockDeviceMapping"
            )
        )
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import aws_sdk_ec2.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            aws_sdk_ec2.types.iam_instance_profile_specification.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import aws_sdk_ec2.types.run_instances_monitoring_enabled

        out["monitoring"] = (
            aws_sdk_ec2.types.run_instances_monitoring_enabled.deserialize_ec2_query(
                child_monitoring
            )
        )
    if el.find("NetworkInterfaces") is not None:
        import aws_sdk_ec2.types.instance_network_interface_specification_list

        out["network_interfaces"] = (
            aws_sdk_ec2.types.instance_network_interface_specification_list.deserialize_ec2_query(
                el, "NetworkInterfaces"
            )
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import aws_sdk_ec2.types.spot_placement

        out["placement"] = aws_sdk_ec2.types.spot_placement.deserialize_ec2_query(
            child_placement
        )
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    return out
