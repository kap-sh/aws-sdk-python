"""Generated from Smithy shape ``com.amazonaws.iot#SetV2LoggingOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.disable_all_logs
    import aws_sdk_iot.types.log_event_configurations
    import aws_sdk_iot.types.log_level


class SetV2LoggingOptionsRequest(TypedDict):
    role_arn: NotRequired["aws_sdk_iot.types.aws_arn.AwsArn"]
    """<p>The ARN of the role that allows IoT to write to Cloudwatch logs.</p>"""
    default_log_level: NotRequired["aws_sdk_iot.types.log_level.LogLevel"]
    """<p>The default logging level.</p>"""
    disable_all_logs: "aws_sdk_iot.types.disable_all_logs.DisableAllLogs"
    """<p>If true all logs are disabled. The default is false.</p>"""
    event_configurations: NotRequired[
        "aws_sdk_iot.types.log_event_configurations.LogEventConfigurations"
    ]
    """<p> The list of event configurations that override account-level logging. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetV2LoggingOptionsRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_log_level" in value:
        import aws_sdk_iot.types.log_level

        out["defaultLogLevel"] = aws_sdk_iot.types.log_level.serialize_json(
            value["default_log_level"]
        )
    out["disableAllLogs"] = value.get("disable_all_logs", False)
    if "event_configurations" in value:
        import aws_sdk_iot.types.log_event_configurations

        out["eventConfigurations"] = (
            aws_sdk_iot.types.log_event_configurations.serialize_json(
                value["event_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetV2LoggingOptionsRequest:
    out: SetV2LoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "defaultLogLevel" in data:
        import aws_sdk_iot.types.log_level

        out["default_log_level"] = aws_sdk_iot.types.log_level.deserialize_json(
            data["defaultLogLevel"]
        )
    if "disableAllLogs" in data:
        out["disable_all_logs"] = data["disableAllLogs"]
    else:
        out["disable_all_logs"] = False
    if "eventConfigurations" in data:
        import aws_sdk_iot.types.log_event_configurations

        out["event_configurations"] = (
            aws_sdk_iot.types.log_event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    return out
