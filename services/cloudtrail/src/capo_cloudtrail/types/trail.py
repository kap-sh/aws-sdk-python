"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Trail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.string


class Trail(TypedDict, closed=True):
    name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Name of the trail set by calling <a>CreateTrail</a>. The maximum length is 128 characters.</p>"""
    s3_bucket_name: NotRequired["capo_cloudtrail.types.string.String"]
    r"""<p>Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html\">Amazon S3 Bucket naming rules</a>.</p>"""
    s3_key_prefix: NotRequired["capo_cloudtrail.types.string.String"]
    r"""<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/get-and-view-cloudtrail-log-files.html#cloudtrail-find-log-files\">Finding Your CloudTrail Log Files</a>. The maximum length is 200 characters.</p>"""
    sns_topic_name: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>This field is no longer in use. Use <code>SnsTopicARN</code>.</p>"""
    sns_topic_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN.</p> <p> <code>arn:aws:sns:us-east-2:123456789012:MyTopic</code> </p>"""
    include_global_service_events: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Set to <b>True</b> to include Amazon Web Services API calls from Amazon Web Services global services such as IAM. Otherwise, <b>False</b>.</p>"""
    is_multi_region_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail exists only in one Region or exists in all Regions.</p>"""
    home_region: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The Region in which the trail was created.</p>"""
    trail_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the trail. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""
    log_file_validation_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether log file validation is enabled.</p>"""
    cloud_watch_logs_log_group_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.</p>"""
    cloud_watch_logs_role_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.</p>"""
    kms_key_id: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>Specifies the KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.</p> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p>"""
    has_custom_event_selectors: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies if the trail has custom event selectors.</p>"""
    has_insight_selectors: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether a trail has insight types specified in an <code>InsightSelector</code> list.</p>"""
    is_organization_trail: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Specifies whether the trail is an organization trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trail) -> dict:
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
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
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
    if "has_custom_event_selectors" in value:
        out["HasCustomEventSelectors"] = value["has_custom_event_selectors"]
    if "has_insight_selectors" in value:
        out["HasInsightSelectors"] = value["has_insight_selectors"]
    if "is_organization_trail" in value:
        out["IsOrganizationTrail"] = value["is_organization_trail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Trail:
    out: Trail = {}  # type: ignore[typeddict-item]
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
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
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
    if "HasCustomEventSelectors" in data:
        out["has_custom_event_selectors"] = data["HasCustomEventSelectors"]
    if "HasInsightSelectors" in data:
        out["has_insight_selectors"] = data["HasInsightSelectors"]
    if "IsOrganizationTrail" in data:
        out["is_organization_trail"] = data["IsOrganizationTrail"]
    return out
