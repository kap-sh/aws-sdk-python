"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateTrailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.boolean
    import aws_sdk_cloudtrail.types.string


class CreateTrailResponse(TypedDict):
    name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the name of the trail.</p>"""
    s3_bucket_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the name of the Amazon S3 bucket designated for publishing log files.</p>"""
    s3_key_prefix: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files\">Finding Your CloudTrail Log Files</a>.</p>"""
    sns_topic_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>This field is no longer in use. Use <code>SnsTopicARN</code>.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:</p> <p> <code>arn:aws:sns:us-east-2:123456789012:MyTopic</code> </p>"""
    include_global_service_events: NotRequired[
        "aws_sdk_cloudtrail.types.boolean.Boolean"
    ]
    """<p>Specifies whether the trail is publishing events from global services such as IAM to the log files.</p>"""
    is_multi_region_trail: NotRequired["aws_sdk_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail exists in one Region or in all Regions.</p>"""
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the trail that was created. The format of a trail ARN is:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""
    log_file_validation_enabled: NotRequired["aws_sdk_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether log file integrity validation is enabled.</p>"""
    cloud_watch_logs_log_group_arn: NotRequired[
        "aws_sdk_cloudtrail.types.string.String"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.</p>"""
    cloud_watch_logs_role_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.</p> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p>"""
    is_organization_trail: NotRequired["aws_sdk_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is an organization trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrailResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "sns_topic_name" in value:
        out["SnsTopicName"] = value["sns_topic_name"]
    if "sns_topic_arn" in value:
        out["SnsTopicARN"] = value["sns_topic_arn"]
    if "include_global_service_events" in value:
        out["IncludeGlobalServiceEvents"] = value["include_global_service_events"]
    if "is_multi_region_trail" in value:
        out["IsMultiRegionTrail"] = value["is_multi_region_trail"]
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "log_file_validation_enabled" in value:
        out["LogFileValidationEnabled"] = value["log_file_validation_enabled"]
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "is_organization_trail" in value:
        out["IsOrganizationTrail"] = value["is_organization_trail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrailResponse:
    out: CreateTrailResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if "SnsTopicName" in data:
        out["sns_topic_name"] = data["SnsTopicName"]
    if "SnsTopicARN" in data:
        out["sns_topic_arn"] = data["SnsTopicARN"]
    if "IncludeGlobalServiceEvents" in data:
        out["include_global_service_events"] = data["IncludeGlobalServiceEvents"]
    if "IsMultiRegionTrail" in data:
        out["is_multi_region_trail"] = data["IsMultiRegionTrail"]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "LogFileValidationEnabled" in data:
        out["log_file_validation_enabled"] = data["LogFileValidationEnabled"]
    if "CloudWatchLogsLogGroupArn" in data:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if "CloudWatchLogsRoleArn" in data:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "IsOrganizationTrail" in data:
        out["is_organization_trail"] = data["IsOrganizationTrail"]
    return out
