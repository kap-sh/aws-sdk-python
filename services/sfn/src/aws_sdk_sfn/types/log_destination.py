"""Generated from Smithy shape ``com.amazonaws.sfn#LogDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.cloud_watch_logs_log_group


class LogDestination(TypedDict):
    cloud_watch_logs_log_group: NotRequired[
        "aws_sdk_sfn.types.cloud_watch_logs_log_group.CloudWatchLogsLogGroup"
    ]
    """<p>An object describing a CloudWatch log group. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html\">AWS::Logs::LogGroup</a> in the CloudFormation User Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestination) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group" in value:
        import aws_sdk_sfn.types.cloud_watch_logs_log_group

        out["cloudWatchLogsLogGroup"] = (
            aws_sdk_sfn.types.cloud_watch_logs_log_group.serialize_aws_json_1_0(
                value["cloud_watch_logs_log_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestination:
    out: LogDestination = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogsLogGroup" in data:
        import aws_sdk_sfn.types.cloud_watch_logs_log_group

        out["cloud_watch_logs_log_group"] = (
            aws_sdk_sfn.types.cloud_watch_logs_log_group.deserialize_aws_json_1_0(
                data["cloudWatchLogsLogGroup"]
            )
        )
    return out
