"""Generated from Smithy shape ``com.amazonaws.ec2#ExportToS3Task``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.container_format
    import aws_sdk_ec2.types.disk_image_format
    import aws_sdk_ec2.types.string


class ExportToS3Task(TypedDict):
    container_format: NotRequired["aws_sdk_ec2.types.container_format.ContainerFormat"]
    """<p>The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.</p>"""
    disk_image_format: NotRequired[
        "aws_sdk_ec2.types.disk_image_format.DiskImageFormat"
    ]
    """<p>The format for the exported image.</p>"""
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon S3 bucket for the destination image. The destination bucket must exist and have an access control list (ACL) attached that specifies the Region-specific canonical account ID for the <code>Grantee</code>. For more information about the ACL to your S3 bucket, see <a href=\"https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#vmexport-prerequisites\">Prerequisites</a> in the VM Import/Export User Guide.</p>"""
    s3_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The encryption key for your S3 bucket.</p>"""
