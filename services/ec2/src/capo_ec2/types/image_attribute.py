"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attribute_value
    import capo_ec2.types.block_device_mapping_list
    import capo_ec2.types.launch_permission_list
    import capo_ec2.types.product_code_list
    import capo_ec2.types.string


class ImageAttribute(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>A description for the AMI.</p>"""
    kernel_id: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The kernel ID.</p>"""
    ramdisk_id: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The RAM disk ID.</p>"""
    sriov_net_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>Indicates whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</p>"""
    boot_mode: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>The boot mode.</p>"""
    tpm_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    """<p>If the image is configured for NitroTPM support, the value is <code>v2.0</code>.</p>"""
    uefi_data: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    r"""<p>Base64 representation of the non-volatile UEFI variable store. To retrieve the UEFI data, use the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData\">GetInstanceUefiData</a> command. You can inspect and modify the UEFI data by using the <a href=\"https://github.com/awslabs/python-uefivars\">python-uefivars tool</a> on GitHub. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html\">UEFI Secure Boot for Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    last_launched_time: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    r"""<p>The date and time, in <a href=\"http://www.iso.org/iso/iso8601\">ISO 8601 date-time format</a>, when the AMI was last used to launch an EC2 instance. When the AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.</p> <note> <p> <code>lastLaunchedTime</code> data is available starting April 2017.</p> </note>"""
    imds_support: NotRequired["capo_ec2.types.attribute_value.AttributeValue"]
    r"""<p>If <code>v2.0</code>, it indicates that IMDSv2 is specified in the AMI. Instances launched from this AMI will have <code>HttpTokens</code> automatically set to <code>required</code> so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, <code>HttpPutResponseHopLimit</code> is set to <code>2</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration\">Configure the AMI</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    deregistration_protection: NotRequired[
        "capo_ec2.types.attribute_value.AttributeValue"
    ]
    """<p>Indicates whether deregistration protection is enabled for the AMI.</p>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    launch_permissions: NotRequired[
        "capo_ec2.types.launch_permission_list.LaunchPermissionList"
    ]
    """<p>The launch permissions.</p>"""
    product_codes: NotRequired["capo_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.block_device_mapping_list.BlockDeviceMappingList"
    ]
    """<p>The block device mapping entries.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "description" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["description"], pairs, f"{prefix}.Description"
        )
    if "kernel_id" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["kernel_id"], pairs, f"{prefix}.Kernel"
        )
    if "ramdisk_id" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["ramdisk_id"], pairs, f"{prefix}.Ramdisk"
        )
    if "sriov_net_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["sriov_net_support"], pairs, f"{prefix}.SriovNetSupport"
        )
    if "boot_mode" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["boot_mode"], pairs, f"{prefix}.BootMode"
        )
    if "tpm_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["tpm_support"], pairs, f"{prefix}.TpmSupport"
        )
    if "uefi_data" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["uefi_data"], pairs, f"{prefix}.UefiData"
        )
    if "last_launched_time" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["last_launched_time"], pairs, f"{prefix}.LastLaunchedTime"
        )
    if "imds_support" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["imds_support"], pairs, f"{prefix}.ImdsSupport"
        )
    if "deregistration_protection" in value:
        import capo_ec2.types.attribute_value

        capo_ec2.types.attribute_value.serialize_ec2_query(
            value["deregistration_protection"],
            pairs,
            f"{prefix}.DeregistrationProtection",
        )
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "launch_permissions" in value:
        import capo_ec2.types.launch_permission_list

        capo_ec2.types.launch_permission_list.serialize_ec2_query(
            value["launch_permissions"], pairs, f"{prefix}.LaunchPermission"
        )
    if "product_codes" in value:
        import capo_ec2.types.product_code_list

        capo_ec2.types.product_code_list.serialize_ec2_query(
            value["product_codes"], pairs, f"{prefix}.ProductCodes"
        )
    if "block_device_mappings" in value:
        import capo_ec2.types.block_device_mapping_list

        capo_ec2.types.block_device_mapping_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{prefix}.BlockDeviceMapping"
        )


def deserialize_ec2_query(el: Element) -> ImageAttribute:
    out: ImageAttribute = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        import capo_ec2.types.attribute_value

        out["description"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_description
        )
    child_kernel_id = el.find("Kernel")
    if child_kernel_id is not None:
        import capo_ec2.types.attribute_value

        out["kernel_id"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_kernel_id
        )
    child_ramdisk_id = el.find("Ramdisk")
    if child_ramdisk_id is not None:
        import capo_ec2.types.attribute_value

        out["ramdisk_id"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_ramdisk_id
        )
    child_sriov_net_support = el.find("SriovNetSupport")
    if child_sriov_net_support is not None:
        import capo_ec2.types.attribute_value

        out["sriov_net_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_sriov_net_support
        )
    child_boot_mode = el.find("BootMode")
    if child_boot_mode is not None:
        import capo_ec2.types.attribute_value

        out["boot_mode"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_boot_mode
        )
    child_tpm_support = el.find("TpmSupport")
    if child_tpm_support is not None:
        import capo_ec2.types.attribute_value

        out["tpm_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_tpm_support
        )
    child_uefi_data = el.find("UefiData")
    if child_uefi_data is not None:
        import capo_ec2.types.attribute_value

        out["uefi_data"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_uefi_data
        )
    child_last_launched_time = el.find("LastLaunchedTime")
    if child_last_launched_time is not None:
        import capo_ec2.types.attribute_value

        out["last_launched_time"] = (
            capo_ec2.types.attribute_value.deserialize_ec2_query(
                child_last_launched_time
            )
        )
    child_imds_support = el.find("ImdsSupport")
    if child_imds_support is not None:
        import capo_ec2.types.attribute_value

        out["imds_support"] = capo_ec2.types.attribute_value.deserialize_ec2_query(
            child_imds_support
        )
    child_deregistration_protection = el.find("DeregistrationProtection")
    if child_deregistration_protection is not None:
        import capo_ec2.types.attribute_value

        out["deregistration_protection"] = (
            capo_ec2.types.attribute_value.deserialize_ec2_query(
                child_deregistration_protection
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    if el.find("LaunchPermission") is not None:
        import capo_ec2.types.launch_permission_list

        out["launch_permissions"] = (
            capo_ec2.types.launch_permission_list.deserialize_ec2_query(
                el, "LaunchPermission"
            )
        )
    if el.find("ProductCodes") is not None:
        import capo_ec2.types.product_code_list

        out["product_codes"] = capo_ec2.types.product_code_list.deserialize_ec2_query(
            el, "ProductCodes"
        )
    if el.find("BlockDeviceMapping") is not None:
        import capo_ec2.types.block_device_mapping_list

        out["block_device_mappings"] = (
            capo_ec2.types.block_device_mapping_list.deserialize_ec2_query(
                el, "BlockDeviceMapping"
            )
        )
    return out
