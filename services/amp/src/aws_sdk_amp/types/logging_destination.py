"""Generated from Smithy shape ``com.amazonaws.amp#LoggingDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.cloud_watch_log_destination
    import aws_sdk_amp.types.logging_filter


class LoggingDestination(TypedDict):
    cloud_watch_logs: (
        "aws_sdk_amp.types.cloud_watch_log_destination.CloudWatchLogDestination"
    )
    """<p>Configuration details for logging to CloudWatch Logs.</p>"""
    filters: "aws_sdk_amp.types.logging_filter.LoggingFilter"
    """<p>Filtering criteria that determine which queries are logged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingDestination) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.cloud_watch_log_destination

    out["cloudWatchLogs"] = (
        aws_sdk_amp.types.cloud_watch_log_destination.serialize_json(
            value["cloud_watch_logs"]
        )
    )
    import aws_sdk_amp.types.logging_filter

    out["filters"] = aws_sdk_amp.types.logging_filter.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> LoggingDestination:
    out: LoggingDestination = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import aws_sdk_amp.types.cloud_watch_log_destination

        out["cloud_watch_logs"] = (
            aws_sdk_amp.types.cloud_watch_log_destination.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    else:
        raise DeserializationError("LoggingDestination.cloud_watch_logs required")
    if "filters" in data:
        import aws_sdk_amp.types.logging_filter

        out["filters"] = aws_sdk_amp.types.logging_filter.deserialize_json(
            data["filters"]
        )
    else:
        raise DeserializationError("LoggingDestination.filters required")
    return out
