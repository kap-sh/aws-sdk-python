"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disk_image_format
    import aws_sdk_ec2.types.export_task_s3_location_request
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class ExportImageRequest(TypedDict):
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Token to enable idempotency for export image requests.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the image being exported. The maximum length is 255 characters.</p>"""
    disk_image_format: NotRequired[
        "aws_sdk_ec2.types.disk_image_format.DiskImageFormat"
    ]
    """<p>The disk image format.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image.</p>"""
    s3_export_location: NotRequired[
        "aws_sdk_ec2.types.export_task_s3_location_request.ExportTaskS3LocationRequest"
    ]
    """<p>The Amazon S3 bucket for the destination image. The destination bucket must exist.</p>"""
    role_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the role that grants VM Import/Export permission to export images to your Amazon S3 bucket. If this parameter is not specified, the default role is named 'vmimport'.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the export image task during creation.</p>"""
