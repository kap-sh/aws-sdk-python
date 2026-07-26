"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_boolean_value
    import capo_ec2.types.attribute_value
    import capo_ec2.types.enclave_options
    import capo_ec2.types.group_identifier_list
    import capo_ec2.types.instance_block_device_mapping_list
    import capo_ec2.types.product_code_list
    import capo_ec2.types.string


class InstanceAttribute(TypedDict, closed=True):
    block_device_mappings: NotRequired[
        "capo_ec2.types.instance_block_device_mapping_list.InstanceBlockDeviceMappingList"
    ]
    """<p>The block device mapping of the instance.</p>"""
    disable_api_termination: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether termination protection is enabled. If the value is <code>true</code>, you can't terminate the instance using the Amazon EC2 console, command line tools, or API.</p>"""
    ena_support: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether enhanced networking with ENA is enabled.</p>"""
    enclave_options: NotRequired["capo_ec2.types.enclave_options.EnclaveOptions"]
    """<p>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</p>"""
    ebs_optimized: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether the instance is optimized for Amazon EBS I/O.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    instance_type: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The instance type.</p>"""
    kernel_id: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The kernel ID.</p>"""
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The RAM disk ID.</p>"""
    root_device_name: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>).</p>"""
    source_dest_check: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether source/destination checks are enabled.</p>"""
    sriov_net_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    user_data: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The user data.</p>"""
    disable_api_stop: NotRequired[
        "capo_ec2.types.attribute_boolean_value.AttributeBooleanValue"
    ]
    """<p>Indicates whether stop protection is enabled for the instance.</p>"""
    groups: NotRequired["capo_ec2.types.group_identifier_list.GroupIdentifierList"]
    """<p>The security groups associated with the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "block_device_mappings" in value:
        import capo_ec2.types.instance_block_device_mapping_list

        capo_ec2.types.instance_block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{prefix}.BlockDeviceMapping"
        )
    if "disable_api_termination" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["disable_api_termination"], pairs, f"{prefix}.DisableApiTermination"
        )
    if "ena_support" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["ena_support"], pairs, f"{prefix}.EnaSupport"
        )
    if "enclave_options" in value:
        import capo_ec2.types.enclave_options

        capo_ec2.types.enclave_options.serialize_ec2_query(
            value["enclave_options"], pairs, f"{prefix}.EnclaveOptions"
        )
    if "ebs_optimized" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["ebs_optimized"], pairs, f"{prefix}.EbsOptimized"
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_initiated_shutdown_behavior" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["instance_initiated_shutdown_behavior"],
            pairs,
            f"{prefix}.InstanceInitiatedShutdownBehavior",
        )
    if "instance_type" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "kernel_id" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["kernel_id"], pairs, f"{prefix}.Kernel"
        )
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )
    if "ramdisk_id" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["ramdisk_id"], pairs, f"{prefix}.Ramdisk"
        )
    if "root_device_name" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["root_device_name"], pairs, f"{prefix}.RootDeviceName"
        )
    if "source_dest_check" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["source_dest_check"], pairs, f"{prefix}.SourceDestCheck"
        )
    if "sriov_net_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["sriov_net_support"], pairs, f"{prefix}.SriovNetSupport"
        )
    if "user_data" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["user_data"], pairs, f"{prefix}.UserData"
        )
    if "disable_api_stop" in value:
        import capo_ec2.types.attribute_boolean_value

        capo_ec2.types.attribute_boolean_value.serialize_ec2_query(
            value["disable_api_stop"], pairs, f"{prefix}.DisableApiStop"
        )
    if "groups" in value:
        import capo_ec2.types.group_identifier_list

        capo_ec2.types.group_identifier_list.serialize_ec2_query(
            value["groups"], pairs, f"{prefix}.GroupSet"
        )


def deserialize_ec2_query(el: Element) -> InstanceAttribute:
    out: InstanceAttribute = {}  # type: ignore[typeddict-item]
    if el.find("BlockDeviceMapping") is not None:
        import capo_ec2.types.instance_block_device_mapping_list

        out["block_device_mappings"] = (
            capo_ec2.types.instance_block_device_mapping_list.deserialize_ec2_query(
                el, "BlockDeviceMapping"
            )
        )
    child_disable_api_termination = el.find("DisableApiTermination")
    if child_disable_api_termination is not None:
        import capo_ec2.types.attribute_boolean_value

        out["disable_api_termination"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_disable_api_termination
            )
        )
    child_ena_support = el.find("EnaSupport")
    if child_ena_support is not None:
        import capo_ec2.types.attribute_boolean_value

        out["ena_support"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_ena_support
            )
        )
    child_enclave_options = el.find("EnclaveOptions")
    if child_enclave_options is not None:
        import capo_ec2.types.enclave_options

        out["enclave_options"] = capo_ec2.types.enclave_options.deserialize_ec2_query(
            child_enclave_options
        )
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        import capo_ec2.types.attribute_boolean_value

        out["ebs_optimized"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_ebs_optimized
            )
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_initiated_shutdown_behavior = el.find(
        "InstanceInitiatedShutdownBehavior"
    )
    if child_instance_initiated_shutdown_behavior is not None:
        import capo_ec2.types.attribute_value

        out["instance_initiated_shutdown_behavior"] = (
            capo_ec2.types.attribute_value.deserialize_ec2_query(
                child_instance_initiated_shutdown_behavior
            )
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.attribute_value

        out["instance_type"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_instance_type
        )
    child_kernel_id = el.find("Kernel")
    if child_kernel_id is not None:
        import capo_ec2.types.attribute_value

        out["kernel_id"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_kernel_id
        )
    if el.find("ProductCodes") is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            el, "ProductCodes"
        )
    child_ramdisk_id = el.find("Ramdisk")
    if child_ramdisk_id is not None:
        import capo_ec2.types.attribute_value

        out["ramdisk_id"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_ramdisk_id
        )
    child_root_device_name = el.find("RootDeviceName")
    if child_root_device_name is not None:
        import capo_ec2.types.attribute_value

        out["root_device_name"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_root_device_name
        )
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        import capo_ec2.types.attribute_boolean_value

        out["source_dest_check"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_source_dest_check
            )
        )
    child_sriov_net_support = el.find("SriovNetSupport")
    if child_sriov_net_support is not None:
        import capo_ec2.types.attribute_value

        out["sriov_net_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_sriov_net_support
        )
    child_user_data = el.find("UserData")
    if child_user_data is not None:
        import capo_ec2.types.attribute_value

        out["user_data"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_user_data
        )
    child_disable_api_stop = el.find("DisableApiStop")
    if child_disable_api_stop is not None:
        import capo_ec2.types.attribute_boolean_value

        out["disable_api_stop"] = (
            capo_ec2.types.attribute_boolean_value.deserialize_ec2_query(
                child_disable_api_stop
            )
        )
    if el.find("GroupSet") is not None:
        import capo_ec2.types.group_identifier_list

        out["groups"] = capo_ec2.types.group_identifier_list.deserialize_ec2_query(
            el, "GroupSet"
        )
    return out
