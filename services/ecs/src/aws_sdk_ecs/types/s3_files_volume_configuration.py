"""Generated from Smithy shape ``com.amazonaws.ecs#S3FilesVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string


class S3FilesVolumeConfiguration(TypedDict):
    file_system_arn: "aws_sdk_ecs.types.string.String"
    """<p>The full ARN of the S3 Files file system to mount.</p>"""
    root_directory: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The directory within the Amazon S3 Files file system to mount as the root directory. If this parameter is omitted, the root of the Amazon S3 Files file system will be used. Specifying <code>/</code> will have the same effect as omitting this parameter.</p> <important> <p>If a S3 Files access point is specified in the <code>accessPointArn</code>, the root directory parameter must either be omitted or set to <code>/</code> which will enforce the path set on the S3 Files access point.</p> </important>"""
    transit_encryption_port: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port to use for sending encrypted data between the ECS host and the S3 Files file system. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon S3 Files mount helper uses. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-mounting.html\">S3 Files mount helper</a>.</p>"""
    access_point_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full ARN of the S3 Files access point to use. If an access point is specified, the root directory value specified in the <code>S3FilesVolumeConfiguration</code> must either be omitted or set to <code>/</code> which will enforce the path set on the S3 Files access point. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html\">Creating S3 Files access points</a>.</p>"""
