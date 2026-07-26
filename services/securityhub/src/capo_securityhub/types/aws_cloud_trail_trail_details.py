"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudTrailTrailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsCloudTrailTrailDetails(TypedDict, closed=True):
    cloud_watch_logs_log_group_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the log group that CloudTrail logs are delivered to.</p>"""
    cloud_watch_logs_role_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the role that the CloudWatch Events endpoint assumes when it writes to the log group.</p>"""
    has_custom_event_selectors: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the trail has custom event selectors.</p>"""
    home_region: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Region where the trail was created.</p>"""
    include_global_service_events: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the trail publishes events from global services such as IAM to the log files.</p>"""
    is_multi_region_trail: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the trail applies only to the current Region or to all Regions.</p>"""
    is_organization_trail: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the trail is created for all accounts in an organization in Organizations, or only for the current Amazon Web Services account.</p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key ID to use to encrypt the logs.</p>"""
    log_file_validation_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether CloudTrail log file validation is enabled.</p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the trail.</p>"""
    s3_bucket_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the S3 bucket where the log files are published.</p>"""
    s3_key_prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The S3 key prefix. The key prefix is added after the name of the S3 bucket where the log files are published.</p>"""
    sns_topic_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the SNS topic that is used for notifications of log file delivery.</p>"""
    sns_topic_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the SNS topic that is used for notifications of log file delivery.</p>"""
    trail_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the trail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudTrailTrailDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "cloud_watch_logs_role_arn" in value:
        out["CloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    if "has_custom_event_selectors" in value:
        out["HasCustomEventSelectors"] = value["has_custom_event_selectors"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "include_global_service_events" in value:
        out["IncludeGlobalServiceEvents"] = value["include_global_service_events"]
    if "is_multi_region_trail" in value:
        out["IsMultiRegionTrail"] = value["is_multi_region_trail"]
    if "is_organization_trail" in value:
        out["IsOrganizationTrail"] = value["is_organization_trail"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "log_file_validation_enabled" in value:
        out["LogFileValidationEnabled"] = value["log_file_validation_enabled"]
    if "name" in value:
        out["Name"] = value["name"]
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "sns_topic_name" in value:
        out["SnsTopicName"] = value["sns_topic_name"]
    if "trail_arn" in value:
        out["TrailArn"] = value["trail_arn"]
    return out


def deserialize_json(data: dict) -> AwsCloudTrailTrailDetails:
    out: AwsCloudTrailTrailDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsLogGroupArn" in data:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if "CloudWatchLogsRoleArn" in data:
        out["cloud_watch_logs_role_arn"] = data["CloudWatchLogsRoleArn"]
    if "HasCustomEventSelectors" in data:
        out["has_custom_event_selectors"] = data["HasCustomEventSelectors"]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "IncludeGlobalServiceEvents" in data:
        out["include_global_service_events"] = data["IncludeGlobalServiceEvents"]
    if "IsMultiRegionTrail" in data:
        out["is_multi_region_trail"] = data["IsMultiRegionTrail"]
    if "IsOrganizationTrail" in data:
        out["is_organization_trail"] = data["IsOrganizationTrail"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "LogFileValidationEnabled" in data:
        out["log_file_validation_enabled"] = data["LogFileValidationEnabled"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3KeyPrefix" in data:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "SnsTopicName" in data:
        out["sns_topic_name"] = data["SnsTopicName"]
    if "TrailArn" in data:
        out["trail_arn"] = data["TrailArn"]
    return out
