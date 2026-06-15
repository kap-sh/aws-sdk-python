"""Generated from Smithy shape ``com.amazonaws.codebuild#CloudWatchLogsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.logs_config_status_type
    import aws_sdk_codebuild.types.string


class CloudWatchLogsConfig(TypedDict):
    status: "aws_sdk_codebuild.types.logs_config_status_type.LogsConfigStatusType"
    """<p>The current status of the logs in CloudWatch Logs for a build project. Valid values are:</p> <ul> <li> <p> <code>ENABLED</code>: CloudWatch Logs are enabled for this build project.</p> </li> <li> <p> <code>DISABLED</code>: CloudWatch Logs are not enabled for this build project.</p> </li> </ul>"""
    group_name: NotRequired["aws_sdk_codebuild.types.string.String"]
    r"""<p> The group name of the logs in CloudWatch Logs. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html\">Working with Log Groups and Log Streams</a>. </p>"""
    stream_name: NotRequired["aws_sdk_codebuild.types.string.String"]
    r"""<p> The prefix of the stream name of the CloudWatch Logs. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html\">Working with Log Groups and Log Streams</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLogsConfig) -> dict:
    out: dict = {}
    import aws_sdk_codebuild.types.logs_config_status_type

    out["status"] = (
        aws_sdk_codebuild.types.logs_config_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLogsConfig:
    out: CloudWatchLogsConfig = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_codebuild.types.logs_config_status_type

        out["status"] = (
            aws_sdk_codebuild.types.logs_config_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CloudWatchLogsConfig.status required")
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    return out
