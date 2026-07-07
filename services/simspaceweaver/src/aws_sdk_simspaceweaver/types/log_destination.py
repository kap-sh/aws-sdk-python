"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group


class LogDestination(TypedDict, closed=True):
    cloud_watch_logs_log_group: NotRequired[
        "aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group.CloudWatchLogsLogGroup"
    ]
    r"""<p>An Amazon CloudWatch Logs log group that stores simulation log data. For more information about log groups, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html\">Working with log groups and log streams</a> in the <i>Amazon CloudWatch Logs User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogDestination) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group" in value:
        import aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group

        out["CloudWatchLogsLogGroup"] = (
            aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group.serialize_json(
                value["cloud_watch_logs_log_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogDestination:
    out: LogDestination = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsLogGroup" in data:
        import aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group

        out["cloud_watch_logs_log_group"] = (
            aws_sdk_simspaceweaver.types.cloud_watch_logs_log_group.deserialize_json(
                data["CloudWatchLogsLogGroup"]
            )
        )
    return out
