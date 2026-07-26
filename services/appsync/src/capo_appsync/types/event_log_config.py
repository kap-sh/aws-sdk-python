"""Generated from Smithy shape ``com.amazonaws.appsync#EventLogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.event_log_level
    import capo_appsync.types.string


class EventLogConfig(TypedDict, closed=True):
    log_level: "capo_appsync.types.event_log_level.EventLogLevel"
    """<p>The type of information to log for the Event API. </p>"""
    cloud_watch_logs_role_arn: "capo_appsync.types.string.String"
    """<p>The IAM service role that AppSync assumes to publish CloudWatch Logs in your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventLogConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.event_log_level

    out["logLevel"] = capo_appsync.types.event_log_level.serialize_json(
        value["log_level"]
    )
    out["cloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    return out


def deserialize_json(data: dict) -> EventLogConfig:
    out: EventLogConfig = {}  # type: ignore[typeddict-item]
    if "logLevel" in data:
        import capo_appsync.types.event_log_level

        out["log_level"] = capo_appsync.types.event_log_level.deserialize_json(
            data["logLevel"]
        )
    else:
        raise DeserializationError("EventLogConfig.log_level required")
    if "cloudWatchLogsRoleArn" in data:
        out["cloud_watch_logs_role_arn"] = data["cloudWatchLogsRoleArn"]
    else:
        raise DeserializationError("EventLogConfig.cloud_watch_logs_role_arn required")
    return out
