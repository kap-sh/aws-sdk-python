"""Generated from Smithy shape ``com.amazonaws.amp#LoggingDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.cloud_watch_log_destination
    import capo_amp.types.logging_filter


class LoggingDestination(TypedDict, closed=True):
    cloud_watch_logs: (
        "capo_amp.types.cloud_watch_log_destination.CloudWatchLogDestination"
    )
    """<p>Configuration details for logging to CloudWatch Logs.</p>"""
    filters: "capo_amp.types.logging_filter.LoggingFilter"
    """<p>Filtering criteria that determine which queries are logged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingDestination) -> dict:
    out: dict = {}
    import capo_amp.types.cloud_watch_log_destination

    out["cloudWatchLogs"] = capo_amp.types.cloud_watch_log_destination.serialize_json(
        value["cloud_watch_logs"]
    )
    import capo_amp.types.logging_filter

    out["filters"] = capo_amp.types.logging_filter.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> LoggingDestination:
    out: LoggingDestination = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import capo_amp.types.cloud_watch_log_destination

        out["cloud_watch_logs"] = (
            capo_amp.types.cloud_watch_log_destination.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    else:
        raise DeserializationError("LoggingDestination.cloud_watch_logs required")
    if "filters" in data:
        import capo_amp.types.logging_filter

        out["filters"] = capo_amp.types.logging_filter.deserialize_json(data["filters"])
    else:
        raise DeserializationError("LoggingDestination.filters required")
    return out
