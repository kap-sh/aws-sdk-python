"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boot_mode_values
    import capo_ec2.types.import_image_license_specification_list_response
    import capo_ec2.types.snapshot_detail_list
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ImportImageTask(TypedDict, closed=True):
    architecture: NotRequired["capo_ec2.types.string.String"]
    """<p>The architecture of the virtual machine.</p> <p>Valid values: <code>i386</code> | <code>x86_64</code> | <code>arm64</code> </p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description of the import task.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image is encrypted.</p>"""
    hypervisor: NotRequired["capo_ec2.types.string.String"]
    """<p>The target hypervisor for the import task.</p> <p>Valid values: <code>xen</code> </p>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Machine Image (AMI) of the imported virtual machine.</p>"""
    import_task_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the import image task.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The identifier for the KMS key that was used to create the encrypted image.</p>"""
    license_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The license type of the virtual machine.</p>"""
    platform: NotRequired["capo_ec2.types.string.String"]
    """<p>The description string for the import image task.</p>"""
    progress: NotRequired["capo_ec2.types.string.String"]
    """<p>The percentage of progress of the import image task.</p>"""
    snapshot_details: NotRequired[
        "capo_ec2.types.snapshot_detail_list.SnapshotDetailList"
    ]
    """<p>Information about the snapshots.</p>"""
    status: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief status for the import image task.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A descriptive status message for the import image task.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the import image task.</p>"""
    license_specifications: NotRequired[
        "capo_ec2.types.import_image_license_specification_list_response.ImportImageLicenseSpecificationListResponse"
    ]
    """<p>The ARNs of the license configurations that are associated with the import image task.</p>"""
    usage_operation: NotRequired["capo_ec2.types.string.String"]
    """<p>The usage operation value.</p>"""
    boot_mode: NotRequired["capo_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the virtual machine.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "architecture" in value:
        pairs.append((f"{prefix}.Architecture", str(value["architecture"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "encrypted" in value:
        pairs.append((f"{prefix}.Encrypted", "true" if value["encrypted"] else "false"))
    if "hypervisor" in value:
        pairs.append((f"{prefix}.Hypervisor", str(value["hypervisor"])))
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "import_task_id" in value:
        pairs.append((f"{prefix}.ImportTaskId", str(value["import_task_id"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "license_type" in value:
        pairs.append((f"{prefix}.LicenseType", str(value["license_type"])))
    if "platform" in value:
        pairs.append((f"{prefix}.Platform", str(value["platform"])))
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "snapshot_details" in value:
        import capo_ec2.types.snapshot_detail_list

        capo_ec2.types.snapshot_detail_list.serialize_ec2_query(
            value["snapshot_details"], pairs, f"{prefix}.SnapshotDetailSet"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "license_specifications" in value:
        import capo_ec2.types.import_image_license_specification_list_response

        capo_ec2.types.import_image_license_specification_list_response.serialize_ec2_query(
            value["license_specifications"], pairs, f"{prefix}.LicenseSpecifications"
        )
    if "usage_operation" in value:
        pairs.append((f"{prefix}.UsageOperation", str(value["usage_operation"])))
    if "boot_mode" in value:
        import capo_ec2.types.boot_mode_values

        capo_ec2.types.boot_mode_values.serialize_ec2_query(
            value["boot_mode"], pairs, f"{prefix}.BootMode"
        )


def deserialize_ec2_query(el: Element) -> ImportImageTask:
    out: ImportImageTask = {}  # type: ignore[typeddict-item]
    child_architecture = el.find("Architecture")
    if child_architecture is not None:
        out["architecture"] = str(child_architecture.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_hypervisor = el.find("Hypervisor")
    if child_hypervisor is not None:
        out["hypervisor"] = str(child_hypervisor.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_import_task_id = el.find("ImportTaskId")
    if child_import_task_id is not None:
        out["import_task_id"] = str(child_import_task_id.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_license_type = el.find("LicenseType")
    if child_license_type is not None:
        out["license_type"] = str(child_license_type.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    if el.find("SnapshotDetailSet") is not None:
        import capo_ec2.types.snapshot_detail_list

        out["snapshot_details"] = (
            capo_ec2.types.snapshot_detail_list.deserialize_ec2_query(
                el, "SnapshotDetailSet"
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    if el.find("LicenseSpecifications") is not None:
        import capo_ec2.types.import_image_license_specification_list_response

        out["license_specifications"] = (
            capo_ec2.types.import_image_license_specification_list_response.deserialize_ec2_query(
                el, "LicenseSpecifications"
            )
        )
    child_usage_operation = el.find("UsageOperation")
    if child_usage_operation is not None:
        out["usage_operation"] = str(child_usage_operation.text or "")
    child_boot_mode = el.find("BootMode")
    if child_boot_mode is not None:
        import capo_ec2.types.boot_mode_values

        out["boot_mode"] = capo_ec2.types.boot_mode_values.deserialize_ec2_query(
            child_boot_mode
        )
    return out
