"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LogPublishingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.cloud_watch_logs_log_group_arn


class LogPublishingOption(TypedDict, closed=True):
    cloud_watch_logs_log_group_arn: NotRequired[
        "capo_elasticsearch_service.types.cloud_watch_logs_log_group_arn.CloudWatchLogsLogGroupArn"
    ]
    enabled: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p> Specifies whether given log publishing option is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogPublishingOption) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group_arn" in value:
        out["CloudWatchLogsLogGroupArn"] = value["cloud_watch_logs_log_group_arn"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> LogPublishingOption:
    out: LogPublishingOption = {}  # type: ignore[typeddict-item]
    if "CloudWatchLogsLogGroupArn" in data:
        out["cloud_watch_logs_log_group_arn"] = data["CloudWatchLogsLogGroupArn"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
