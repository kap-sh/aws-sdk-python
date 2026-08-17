"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.string


class ExecuteCommandLogConfiguration(TypedDict, closed=True):
    cloud_watch_log_group_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the CloudWatch log group to send logs to.</p> <note> <p>The CloudWatch log group must already be created.</p> </note>"""
    cloud_watch_encryption_enabled: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use encryption on the CloudWatch logs. If not specified, encryption will be off.</p>"""
    s3_bucket_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the S3 bucket to send logs to.</p> <note> <p>The S3 bucket must already be created.</p> </note>"""
    s3_encryption_enabled: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use encryption on the S3 logs. If not specified, encryption is not used.</p>"""
    s3_key_prefix: NotRequired["capo_ecs.types.string.String"]
    """<p>An optional folder in the S3 bucket to place logs in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandLogConfiguration) -> dict:
    out: dict = {}
    if "cloud_watch_log_group_name" in value:
        out["cloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    out["cloudWatchEncryptionEnabled"] = value.get(
        "cloud_watch_encryption_enabled", False
    )
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    out["s3EncryptionEnabled"] = value.get("s3_encryption_enabled", False)
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteCommandLogConfiguration:
    out: ExecuteCommandLogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogGroupName") is not None:
        out["cloud_watch_log_group_name"] = data["cloudWatchLogGroupName"]
    if data.get("cloudWatchEncryptionEnabled") is not None:
        out["cloud_watch_encryption_enabled"] = data["cloudWatchEncryptionEnabled"]
    else:
        out["cloud_watch_encryption_enabled"] = False
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("s3EncryptionEnabled") is not None:
        out["s3_encryption_enabled"] = data["s3EncryptionEnabled"]
    else:
        out["s3_encryption_enabled"] = False
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    return out
