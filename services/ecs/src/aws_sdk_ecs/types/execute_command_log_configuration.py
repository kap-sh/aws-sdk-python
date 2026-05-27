"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandLogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string


class ExecuteCommandLogConfiguration(TypedDict):
    cloud_watch_log_group_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the CloudWatch log group to send logs to.</p> <note> <p>The CloudWatch log group must already be created.</p> </note>"""
    cloud_watch_encryption_enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off.</p>"""
    s3_bucket_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the S3 bucket to send logs to.</p> <note> <p>The S3 bucket must already be created.</p> </note>"""
    s3_encryption_enabled: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use encryption on the S3 logs. If not specified, encryption is not used.</p>"""
    s3_key_prefix: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>An optional folder in the S3 bucket to place logs in.</p>"""
