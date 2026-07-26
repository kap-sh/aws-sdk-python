"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainLogPublishingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainLogPublishingOption(TypedDict, closed=True):
    cloud_watch_logs_log_group_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the CloudWatch Logs group to publish the logs to.</p>"""
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the log publishing is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainLogPublishingOption) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainLogPublishingOption:
    out: AwsOpenSearchServiceDomainLogPublishingOption = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsLogGroupArn" in data:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
