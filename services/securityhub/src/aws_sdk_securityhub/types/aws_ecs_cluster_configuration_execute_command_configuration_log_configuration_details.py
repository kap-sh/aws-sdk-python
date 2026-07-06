"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails(
    TypedDict, closed=True
):
    cloud_watch_encryption_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether to enable encryption on the CloudWatch logs.</p>"""
    cloud_watch_log_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the CloudWatch log group to send the logs to.</p>"""
    s3_bucket_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the S3 bucket to send logs to.</p>"""
    s3_encryption_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to encrypt the logs that are sent to the S3 bucket.</p>"""
    s3_key_prefix: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Identifies the folder in the S3 bucket to send the logs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails,
) -> dict:
    out: dict = {}
    if "cloud_watch_encryption_enabled" in value:
        out["CloudWatchEncryptionEnabled"] = value["cloud_watch_encryption_enabled"]
    if "cloud_watch_log_group_name" in value:
        out["CloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_encryption_enabled" in value:
        out["S3EncryptionEnabled"] = value["s3_encryption_enabled"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails:
    out: AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchEncryptionEnabled" in data:
        out["cloud_watch_encryption_enabled"] = data["CloudWatchEncryptionEnabled"]
    if "CloudWatchLogGroupName" in data:
        out["cloud_watch_log_group_name"] = data["CloudWatchLogGroupName"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3EncryptionEnabled" in data:
        out["s3_encryption_enabled"] = data["S3EncryptionEnabled"]
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
