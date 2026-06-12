"""Generated from Smithy shape ``com.amazonaws.appsync#EventLogConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.event_log_level
    import aws_sdk_appsync.types.string


class EventLogConfig(TypedDict):
    log_level: "aws_sdk_appsync.types.event_log_level.EventLogLevel"
    """<p>The type of information to log for the Event API. </p>"""
    cloud_watch_logs_role_arn: "aws_sdk_appsync.types.string.String"
    """<p>The IAM service role that AppSync assumes to publish CloudWatch Logs in your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventLogConfig) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.event_log_level

    out["logLevel"] = aws_sdk_appsync.types.event_log_level.serialize_json(
        value["log_level"]
    )
    out["cloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    return out


def deserialize_json(data: dict) -> EventLogConfig:
    out: EventLogConfig = {}  # type: ignore[typeddict-item]
    if "logLevel" in data:
        import aws_sdk_appsync.types.event_log_level

        out["log_level"] = aws_sdk_appsync.types.event_log_level.deserialize_json(
            data["logLevel"]
        )
    else:
        raise DeserializationError("EventLogConfig.log_level required")
    if "cloudWatchLogsRoleArn" in data:
        out["cloud_watch_logs_role_arn"] = data["cloudWatchLogsRoleArn"]
    else:
        raise DeserializationError("EventLogConfig.cloud_watch_logs_role_arn required")
    return out
