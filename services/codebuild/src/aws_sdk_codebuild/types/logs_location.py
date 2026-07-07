"""Generated from Smithy shape ``com.amazonaws.codebuild#LogsLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.cloud_watch_logs_config
    import aws_sdk_codebuild.types.s3_logs_config
    import aws_sdk_codebuild.types.string


class LogsLocation(TypedDict, closed=True):
    group_name: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The name of the CloudWatch Logs group for the build logs.</p>"""
    stream_name: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The name of the CloudWatch Logs stream for the build logs.</p>"""
    deep_link: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The URL to an individual build log in CloudWatch Logs. The log stream is created during the PROVISIONING phase of a build and the <code>deeplink</code> will not be valid until it is created.</p>"""
    s3_deep_link: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> The URL to a build log in an S3 bucket. </p>"""
    cloud_watch_logs_arn: NotRequired["aws_sdk_codebuild.types.string.String"]
    r"""<p>The ARN of the CloudWatch Logs stream for a build execution. Its format is <code>arn:${Partition}:logs:${Region}:${Account}:log-group:${LogGroupName}:log-stream:${LogStreamName}</code>. The CloudWatch Logs stream is created during the PROVISIONING phase of a build and the ARN will not be valid until it is created. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatchlogs.html#amazoncloudwatchlogs-resources-for-iam-policies\">Resources Defined by CloudWatch Logs</a>.</p>"""
    s3_logs_arn: NotRequired["aws_sdk_codebuild.types.string.String"]
    r"""<p> The ARN of S3 logs for a build project. Its format is <code>arn:${Partition}:s3:::${BucketName}/${ObjectName}</code>. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html#amazons3-resources-for-iam-policies\">Resources Defined by Amazon S3</a>. </p>"""
    cloud_watch_logs: NotRequired[
        "aws_sdk_codebuild.types.cloud_watch_logs_config.CloudWatchLogsConfig"
    ]
    """<p> Information about CloudWatch Logs for a build project. </p>"""
    s3_logs: NotRequired["aws_sdk_codebuild.types.s3_logs_config.S3LogsConfig"]
    """<p> Information about S3 logs for a build project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogsLocation) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "deep_link" in value:
        out["deepLink"] = value["deep_link"]
    if "s3_deep_link" in value:
        out["s3DeepLink"] = value["s3_deep_link"]
    if "cloud_watch_logs_arn" in value:
        out["cloudWatchLogsArn"] = value["cloud_watch_logs_arn"]
    if "s3_logs_arn" in value:
        out["s3LogsArn"] = value["s3_logs_arn"]
    if "cloud_watch_logs" in value:
        import aws_sdk_codebuild.types.cloud_watch_logs_config

        out["cloudWatchLogs"] = (
            aws_sdk_codebuild.types.cloud_watch_logs_config.serialize_aws_json_1_1(
                value["cloud_watch_logs"]
            )
        )
    if "s3_logs" in value:
        import aws_sdk_codebuild.types.s3_logs_config

        out["s3Logs"] = aws_sdk_codebuild.types.s3_logs_config.serialize_aws_json_1_1(
            value["s3_logs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LogsLocation:
    out: LogsLocation = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    if "deepLink" in data:
        out["deep_link"] = data["deepLink"]
    if "s3DeepLink" in data:
        out["s3_deep_link"] = data["s3DeepLink"]
    if "cloudWatchLogsArn" in data:
        out["cloud_watch_logs_arn"] = data["cloudWatchLogsArn"]
    if "s3LogsArn" in data:
        out["s3_logs_arn"] = data["s3LogsArn"]
    if "cloudWatchLogs" in data:
        import aws_sdk_codebuild.types.cloud_watch_logs_config

        out["cloud_watch_logs"] = (
            aws_sdk_codebuild.types.cloud_watch_logs_config.deserialize_aws_json_1_1(
                data["cloudWatchLogs"]
            )
        )
    if "s3Logs" in data:
        import aws_sdk_codebuild.types.s3_logs_config

        out["s3_logs"] = (
            aws_sdk_codebuild.types.s3_logs_config.deserialize_aws_json_1_1(
                data["s3Logs"]
            )
        )
    return out
