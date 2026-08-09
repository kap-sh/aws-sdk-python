"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesLaunchSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.kernel_id
    import capo_ec2.types.key_pair_name
    import capo_ec2.types.ramdisk_id
    import capo_ec2.types.scheduled_instances_block_device_mapping_set
    import capo_ec2.types.scheduled_instances_iam_instance_profile
    import capo_ec2.types.scheduled_instances_monitoring
    import capo_ec2.types.scheduled_instances_network_interface_set
    import capo_ec2.types.scheduled_instances_placement
    import capo_ec2.types.scheduled_instances_security_group_id_set
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class ScheduledInstancesLaunchSpecification(TypedDict, closed=True):
    block_device_mappings: NotRequired[
        "capo_ec2.types.scheduled_instances_block_device_mapping_set.ScheduledInstancesBlockDeviceMappingSet"
    ]
    """<p>The block device mapping entries.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the instances are optimized for EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal EBS I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.</p> <p>Default: <code>false</code> </p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.scheduled_instances_iam_instance_profile.ScheduledInstancesIamInstanceProfile"
    ]
    """<p>The IAM instance profile.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the Amazon Machine Image (AMI).</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["capo_ec2.types.kernel_id.KernelId"]
    """<p>The ID of the kernel.</p>"""
    key_name: NotRequired["capo_ec2.types.key_pair_name.KeyPairName"]
    """<p>The name of the key pair.</p>"""
    monitoring: NotRequired[
        "capo_ec2.types.scheduled_instances_monitoring.ScheduledInstancesMonitoring"
    ]
    """<p>Enable or disable monitoring for the instances.</p>"""
    network_interfaces: NotRequired[
        "capo_ec2.types.scheduled_instances_network_interface_set.ScheduledInstancesNetworkInterfaceSet"
    ]
    """<p>The network interfaces.</p>"""
    placement: NotRequired[
        "capo_ec2.types.scheduled_instances_placement.ScheduledInstancesPlacement"
    ]
    """<p>The placement information.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.ramdisk_id.RamdiskId"]
    """<p>The ID of the RAM disk.</p>"""
    security_group_ids: NotRequired[
        "capo_ec2.types.scheduled_instances_security_group_id_set.ScheduledInstancesSecurityGroupIdSet"
    ]
    """<p>The IDs of the security groups.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to launch the instances.</p>"""
    user_data: NotRequired["capo_ec2.types.string.String"]
    """<p>The base64-encoded MIME user data.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesLaunchSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "block_device_mappings" in value:
        import capo_ec2.types.scheduled_instances_block_device_mapping_set

        capo_ec2.types.scheduled_instances_block_device_mapping_set.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.scheduled_instances_iam_instance_profile

        capo_ec2.types.scheduled_instances_iam_instance_profile.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "kernel_id" in value:
        pairs.append((f"{key_prefix}KernelId", str(value["kernel_id"])))
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "monitoring" in value:
        import capo_ec2.types.scheduled_instances_monitoring

        capo_ec2.types.scheduled_instances_monitoring.serialize_ec2_query(
            value["monitoring"], pairs, f"{key_prefix}Monitoring"
        )
    if "network_interfaces" in value:
        import capo_ec2.types.scheduled_instances_network_interface_set

        capo_ec2.types.scheduled_instances_network_interface_set.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{key_prefix}NetworkInterface"
        )
    if "placement" in value:
        import capo_ec2.types.scheduled_instances_placement

        capo_ec2.types.scheduled_instances_placement.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "ramdisk_id" in value:
        pairs.append((f"{key_prefix}RamdiskId", str(value["ramdisk_id"])))
    if "security_group_ids" in value:
        import capo_ec2.types.scheduled_instances_security_group_id_set

        capo_ec2.types.scheduled_instances_security_group_id_set.serialize_ec2_query(
            value["security_group_ids"], pairs, f"{key_prefix}SecurityGroupId"
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "user_data" in value:
        pairs.append((f"{key_prefix}UserData", str(value["user_data"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesLaunchSpecification:
    out: ScheduledInstancesLaunchSpecification = {}  # type: ignore[typeddict-item]
    child_block_device_mappings = el.find("BlockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.scheduled_instances_block_device_mapping_set

        out["block_device_mappings"] = (
            capo_ec2.types.scheduled_instances_block_device_mapping_set.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.scheduled_instances_iam_instance_profile

        out["iam_instance_profile"] = (
            capo_ec2.types.scheduled_instances_iam_instance_profile.deserialize_ec2_query(
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
        import capo_ec2.types.scheduled_instances_monitoring

        out["monitoring"] = (
            capo_ec2.types.scheduled_instances_monitoring.deserialize_ec2_query(
                child_monitoring
            )
        )
    child_network_interfaces = el.find("NetworkInterface")
    if child_network_interfaces is not None:
        import capo_ec2.types.scheduled_instances_network_interface_set

        out["network_interfaces"] = (
            capo_ec2.types.scheduled_instances_network_interface_set.deserialize_ec2_query(
                child_network_interfaces
            )
        )
    child_placement = el.find("Placement")
    if child_placement is not None:
        import capo_ec2.types.scheduled_instances_placement

        out["placement"] = (
            capo_ec2.types.scheduled_instances_placement.deserialize_ec2_query(
                child_placement
            )
        )
    child_ramdisk_id = el.find("RamdiskId")
    if child_ramdisk_id is not None:
        out["ramdisk_id"] = str(child_ramdisk_id.text or "")
    child_security_group_ids = el.find("SecurityGroupId")
    if child_security_group_ids is not None:
        import capo_ec2.types.scheduled_instances_security_group_id_set

        out["security_group_ids"] = (
            capo_ec2.types.scheduled_instances_security_group_id_set.deserialize_ec2_query(
                child_security_group_ids
            )
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        out["user_data"] = str(child_user_data.text or "")
    return out
