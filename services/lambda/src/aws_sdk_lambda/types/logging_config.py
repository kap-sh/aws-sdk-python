"""Generated from Smithy shape ``com.amazonaws.lambda#LoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.application_log_level
    import aws_sdk_lambda.types.log_format
    import aws_sdk_lambda.types.log_group
    import aws_sdk_lambda.types.system_log_level


class LoggingConfig(TypedDict, closed=True):
    log_format: NotRequired["aws_sdk_lambda.types.log_format.LogFormat"]
    """<p>The format in which Lambda sends your function's application and system logs to CloudWatch. Select between plain text and structured JSON.</p>"""
    application_log_level: NotRequired[
        "aws_sdk_lambda.types.application_log_level.ApplicationLogLevel"
    ]
    """<p>Set this property to filter the application logs for your function that Lambda sends to CloudWatch. Lambda only sends application logs at the selected level of detail and lower, where <code>TRACE</code> is the highest level and <code>FATAL</code> is the lowest.</p>"""
    system_log_level: NotRequired[
        "aws_sdk_lambda.types.system_log_level.SystemLogLevel"
    ]
    """<p>Set this property to filter the system logs for your function that Lambda sends to CloudWatch. Lambda only sends system logs at the selected level of detail and lower, where <code>DEBUG</code> is the highest level and <code>WARN</code> is the lowest.</p>"""
    log_group: NotRequired["aws_sdk_lambda.types.log_group.LogGroup"]
    """<p>The name of the Amazon CloudWatch log group the function sends logs to. By default, Lambda functions send logs to a default log group named <code>/aws/lambda/&lt;function name&gt;</code>. To use a different log group, enter an existing log group or enter a new log group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfig) -> dict:
    out: dict = {}
    if "log_format" in value:
        import aws_sdk_lambda.types.log_format

        out["LogFormat"] = aws_sdk_lambda.types.log_format.serialize_json(
            value["log_format"]
        )
    if "application_log_level" in value:
        import aws_sdk_lambda.types.application_log_level

        out["ApplicationLogLevel"] = (
            aws_sdk_lambda.types.application_log_level.serialize_json(
                value["application_log_level"]
            )
        )
    if "system_log_level" in value:
        import aws_sdk_lambda.types.system_log_level

        out["SystemLogLevel"] = aws_sdk_lambda.types.system_log_level.serialize_json(
            value["system_log_level"]
        )
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    return out


def deserialize_json(data: dict) -> LoggingConfig:
    out: LoggingConfig = {}  # type: ignore[typeddict-item]
    if "LogFormat" in data:
        import aws_sdk_lambda.types.log_format

        out["log_format"] = aws_sdk_lambda.types.log_format.deserialize_json(
            data["LogFormat"]
        )
    if "ApplicationLogLevel" in data:
        import aws_sdk_lambda.types.application_log_level

        out["application_log_level"] = (
            aws_sdk_lambda.types.application_log_level.deserialize_json(
                data["ApplicationLogLevel"]
            )
        )
    if "SystemLogLevel" in data:
        import aws_sdk_lambda.types.system_log_level

        out["system_log_level"] = (
            aws_sdk_lambda.types.system_log_level.deserialize_json(
                data["SystemLogLevel"]
            )
        )
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    return out
