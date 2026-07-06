"""Generated from Smithy shape ``com.amazonaws.iot#LogEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_destination
    import aws_sdk_iot.types.log_event_type
    import aws_sdk_iot.types.log_level


class LogEventConfiguration(TypedDict, closed=True):
    event_type: "aws_sdk_iot.types.log_event_type.LogEventType"
    """<p> The type of event to log. These include event types like Connect, Publish, and Disconnect. </p>"""
    log_level: NotRequired["aws_sdk_iot.types.log_level.LogLevel"]
    """<p> The logging level for the specified event type. Determines the verbosity of log messages generated for this event type. </p>"""
    log_destination: NotRequired["aws_sdk_iot.types.log_destination.LogDestination"]
    """<p> CloudWatch Log Group for event-based logging. Specifies where log events should be sent. The log destination for event-based logging overrides default Log Group for the specified event type and applies to all resources associated with that event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogEventConfiguration) -> dict:
    out: dict = {}
    out["eventType"] = value["event_type"]
    if "log_level" in value:
        import aws_sdk_iot.types.log_level

        out["logLevel"] = aws_sdk_iot.types.log_level.serialize_json(value["log_level"])
    if "log_destination" in value:
        out["logDestination"] = value["log_destination"]
    return out


def deserialize_json(data: dict) -> LogEventConfiguration:
    out: LogEventConfiguration = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("LogEventConfiguration.event_type required")
    if "logLevel" in data:
        import aws_sdk_iot.types.log_level

        out["log_level"] = aws_sdk_iot.types.log_level.deserialize_json(
            data["logLevel"]
        )
    if "logDestination" in data:
        out["log_destination"] = data["logDestination"]
    return out
