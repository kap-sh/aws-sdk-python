"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boot_mode_values
    import aws_sdk_ec2.types.import_image_license_specification_list_response
    import aws_sdk_ec2.types.snapshot_detail_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ImportImageTask(TypedDict):
    architecture: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The architecture of the virtual machine.</p> <p>Valid values: <code>i386</code> | <code>x86_64</code> | <code>arm64</code> </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the import task.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the image is encrypted.</p>"""
    hypervisor: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target hypervisor for the import task.</p> <p>Valid values: <code>xen</code> </p>"""
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Machine Image (AMI) of the imported virtual machine.</p>"""
    import_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the import image task.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The identifier for the KMS key that was used to create the encrypted image.</p>"""
    license_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The license type of the virtual machine.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description string for the import image task.</p>"""
    progress: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The percentage of progress of the import image task.</p>"""
    snapshot_details: NotRequired[
        "aws_sdk_ec2.types.snapshot_detail_list.SnapshotDetailList"
    ]
    """<p>Information about the snapshots.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief status for the import image task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A descriptive status message for the import image task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the import image task.</p>"""
    license_specifications: NotRequired[
        "aws_sdk_ec2.types.import_image_license_specification_list_response.ImportImageLicenseSpecificationListResponse"
    ]
    """<p>The ARNs of the license configurations that are associated with the import image task.</p>"""
    usage_operation: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The usage operation value.</p>"""
    boot_mode: NotRequired["aws_sdk_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the virtual machine.</p>"""
