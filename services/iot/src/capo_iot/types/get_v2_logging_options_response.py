"""Generated from Smithy shape ``com.amazonaws.iot#GetV2LoggingOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.disable_all_logs
    import capo_iot.types.log_event_configurations
    import capo_iot.types.log_level


class GetV2LoggingOptionsResponse(TypedDict, closed=True):
    role_arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>The IAM role ARN IoT uses to write to your CloudWatch logs.</p>"""
    default_log_level: NotRequired["capo_iot.types.log_level.LogLevel"]
    """<p>The default log level.</p>"""
    disable_all_logs: "capo_iot.types.disable_all_logs.DisableAllLogs"
    """<p>Disables all logs.</p>"""
    event_configurations: NotRequired[
        "capo_iot.types.log_event_configurations.LogEventConfigurations"
    ]
    """<p> The list of event configurations that override account-level logging. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetV2LoggingOptionsResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_log_level" in value:
        import capo_iot.types.log_level

        out["defaultLogLevel"] = capo_iot.types.log_level.serialize_json(
            value["default_log_level"]
        )
    out["disableAllLogs"] = value.get("disable_all_logs", False)
    if "event_configurations" in value:
        import capo_iot.types.log_event_configurations

        out["eventConfigurations"] = (
            capo_iot.types.log_event_configurations.serialize_json(
                value["event_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetV2LoggingOptionsResponse:
    out: GetV2LoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "defaultLogLevel" in data:
        import capo_iot.types.log_level

        out["default_log_level"] = capo_iot.types.log_level.deserialize_json(
            data["defaultLogLevel"]
        )
    if "disableAllLogs" in data:
        out["disable_all_logs"] = data["disableAllLogs"]
    else:
        out["disable_all_logs"] = False
    if "eventConfigurations" in data:
        import capo_iot.types.log_event_configurations

        out["event_configurations"] = (
            capo_iot.types.log_event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    return out
