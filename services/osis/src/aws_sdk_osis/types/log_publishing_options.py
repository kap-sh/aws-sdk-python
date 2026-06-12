"""Generated from Smithy shape ``com.amazonaws.osis#LogPublishingOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_osis.types.boolean
    import aws_sdk_osis.types.cloud_watch_log_destination


class LogPublishingOptions(TypedDict):
    is_logging_enabled: NotRequired["aws_sdk_osis.types.boolean.Boolean"]
    """<p>Whether logs should be published.</p>"""
    cloud_watch_log_destination: NotRequired[
        "aws_sdk_osis.types.cloud_watch_log_destination.CloudWatchLogDestination"
    ]
    """<p>The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if <code>IsLoggingEnabled</code> is set to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogPublishingOptions) -> dict:
    out: dict = {}
    if "is_logging_enabled" in value:
        out["IsLoggingEnabled"] = value["is_logging_enabled"]
    if "cloud_watch_log_destination" in value:
        import aws_sdk_osis.types.cloud_watch_log_destination

        out["CloudWatchLogDestination"] = (
            aws_sdk_osis.types.cloud_watch_log_destination.serialize_json(
                value["cloud_watch_log_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> LogPublishingOptions:
    out: LogPublishingOptions = {}  # type: ignore[typeddict-item]
    if "IsLoggingEnabled" in data:
        out["is_logging_enabled"] = data["IsLoggingEnabled"]
    if "CloudWatchLogDestination" in data:
        import aws_sdk_osis.types.cloud_watch_log_destination

        out["cloud_watch_log_destination"] = (
            aws_sdk_osis.types.cloud_watch_log_destination.deserialize_json(
                data["CloudWatchLogDestination"]
            )
        )
    return out
