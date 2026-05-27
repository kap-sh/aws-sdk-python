"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
