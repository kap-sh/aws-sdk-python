"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53QueryLoggingConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details


class AwsRoute53QueryLoggingConfigDetails(TypedDict, closed=True):
    cloud_watch_logs_log_group_arn: NotRequired[
        "aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details.CloudWatchLogsLogGroupArnConfigDetails"
    ]
    """<p> The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log group that Route 53 is publishing logs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53QueryLoggingConfigDetails) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group_arn" in value:
        import aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details

        out["CloudWatchLogsLogGroupArn"] = (
            aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details.serialize_json(
                value["cloud_watch_logs_log_group_arn"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRoute53QueryLoggingConfigDetails:
    out: AwsRoute53QueryLoggingConfigDetails = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsLogGroupArn" in data:
        import aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details

        out["cloud_watch_logs_log_group_arn"] = (
            aws_sdk_securityhub.types.cloud_watch_logs_log_group_arn_config_details.deserialize_json(
                data["CloudWatchLogsLogGroupArn"]
            )
        )
    return out
