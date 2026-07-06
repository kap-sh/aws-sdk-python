"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesLaunchSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

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


class ScheduledInstancesLaunchSpecification(TypedDict, closed=True):
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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesLaunchSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "block_device_mappings" in value:
        import aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set

        aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{prefix}.BlockDeviceMappings"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import aws_sdk_ec2.types.scheduled_instances_iam_instance_profile

        aws_sdk_ec2.types.scheduled_instances_iam_instance_profile.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{prefix}.IamInstanceProfile"
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "kernel_id" in value:
        pairs.append((f"{prefix}.KernelId", str(value["kernel_id"])))
    if "key_name" in value:
        pairs.append((f"{prefix}.KeyName", str(value["key_name"])))
    if "monitoring" in value:
        import aws_sdk_ec2.types.scheduled_instances_monitoring

        aws_sdk_ec2.types.scheduled_instances_monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{prefix}.Monitoring"
        )
    if "network_interfaces" in value:
        import aws_sdk_ec2.types.scheduled_instances_network_interface_set

        aws_sdk_ec2.types.scheduled_instances_network_interface_set.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{prefix}.NetworkInterfaces"
        )
    if "placement" in value:
        import aws_sdk_ec2.types.scheduled_instances_placement

        aws_sdk_ec2.types.scheduled_instances_placement.serialize_ec2_query(
            value["placement"], pairs, f"{prefix}.Placement"
        )
    if "ramdisk_id" in value:
        pairs.append((f"{prefix}.RamdiskId", str(value["ramdisk_id"])))
    if "security_group_ids" in value:
        import aws_sdk_ec2.types.scheduled_instances_security_group_id_set

        aws_sdk_ec2.types.scheduled_instances_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{prefix}.SecurityGroupIds"
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "user_data" in value:
        pairs.append((f"{prefix}.UserData", str(value["user_data"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesLaunchSpecification:
    out: ScheduledInstancesLaunchSpecification = {}  # type: ignore[typeddict-item]
    if el.find("BlockDeviceMappings") is not None:
        import aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set

        out["block_device_mappings"] = (
            aws_sdk_ec2.types.scheduled_instances_block_device_mapping_set.deserialize_ec2_query(
                el, "BlockDeviceMappings"
            )
        )
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import aws_sdk_ec2.types.scheduled_instances_iam_instance_profile

        out["iam_instance_profile"] = (
            aws_sdk_ec2.types.scheduled_instances_iam_instance_profile.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_kernel_id = el.find("KernelId")
    if child_kernel_id is not None:
        out["kernel_id"] = str(child_kernel_id.text or "")
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_monitoring = el.find("Monitoring")
    if child_monitoring is not None:
        import aws_sdk_ec2.types.scheduled_instances_monitoring

        out["monitoring"] = (
            aws_sdk_ec2.types.scheduled_instances_monitoring.deserialize_ec2_query(
                child_monitoring
            )
        )
    if el.find("NetworkInterfaces") is not None:
        import aws_sdk_ec2.types.scheduled_instances_network_interface_set

        out["network_interfaces"] = (
            aws_sdk_ec2.types.scheduled_instances_network_interface_set.deserialize_ec2_query(
                el, "NetworkInterfaces"
            )
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import aws_sdk_ec2.types.scheduled_instances_placement

        out["placement"] = (
            aws_sdk_ec2.types.scheduled_instances_placement.deserialize_ec2_query(
                child_placement
            )
        )
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    if el.find("SecurityGroupIds") is not None:
        import aws_sdk_ec2.types.scheduled_instances_security_group_id_set

        out["security_group_ids"] = (
            aws_sdk_ec2.types.scheduled_instances_security_group_id_set.deserialize_ec2_query(
                el, "SecurityGroupIds"
            )
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    return out
