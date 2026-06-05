"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.import_image_license_specification_list_response
    import aws_sdk_ec2.types.import_image_task_id
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.snapshot_detail_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportImageResult(TypedDict):
    architecture: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The architecture of the virtual machine.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the import task.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AMI is encrypted.</p>"""
    hypervisor: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target hypervisor of the import task.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Machine Image (AMI) created by the import task.</p>"""
    import_task_id: NotRequired[
        "aws_sdk_ec2.types.import_image_task_id.ImportImageTaskId"
    ]
    """<p>The task ID of the import image task.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier for the symmetric KMS key that was used to create the encrypted AMI.</p>"""
    license_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The license type of the virtual machine.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The operating system of the virtual machine.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The progress of the task.</p>"""
    snapshot_details: NotRequired[
        "aws_sdk_ec2.types.snapshot_detail_list.SnapshotDetailList"
    ]
    """<p>Information about the snapshots.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief status of the task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A detailed status message of the import task.</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.import_image_license_specification_list_response.ImportImageLicenseSpecificationListResponse"
    ]
    """<p>The ARNs of the license configurations.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the import image task.</p>"""
    usage_operation: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The usage operation value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageResult, pairs: list[tuple[str, str]], prefix: str
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
        import aws_sdk_ec2.types.snapshot_detail_list

        aws_sdk_ec2.types.snapshot_detail_list.serialize_ec2_query(
            value["snapshot_details"], pairs, f"{prefix}.SnapshotDetailSet"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "license_specifications" in value:
        import aws_sdk_ec2.types.import_image_license_specification_list_response

        aws_sdk_ec2.types.import_image_license_specification_list_response.serialize_ec2_query(
            value["license_specifications"], pairs, f"{prefix}.LicenseSpecifications"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "usage_operation" in value:
        pairs.append((f"{prefix}.UsageOperation", str(value["usage_operation"])))


def deserialize_ec2_query(el: Element) -> ImportImageResult:
    out: ImportImageResult = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_ec2.types.snapshot_detail_list

        out["snapshot_details"] = (
            aws_sdk_ec2.types.snapshot_detail_list.deserialize_ec2_query(
                el, "SnapshotDetailSet"
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("LicenseSpecifications") is not None:
        import aws_sdk_ec2.types.import_image_license_specification_list_response

        out["license_specifications"] = (
            aws_sdk_ec2.types.import_image_license_specification_list_response.deserialize_ec2_query(
                el, "LicenseSpecifications"
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_usage_operation = el.find("UsageOperation")
    if child_usage_operation is not None:
        out["usage_operation"] = str(child_usage_operation.text or "")
    return out
