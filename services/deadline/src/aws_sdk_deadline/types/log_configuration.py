"""Generated from Smithy shape ``com.amazonaws.deadline#LogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.log_driver
    import aws_sdk_deadline.types.log_error
    import aws_sdk_deadline.types.log_options
    import aws_sdk_deadline.types.log_parameters


class LogConfiguration(TypedDict, closed=True):
    log_driver: "aws_sdk_deadline.types.log_driver.LogDriver"
    """<p>The log drivers for worker related logs.</p>"""
    options: NotRequired["aws_sdk_deadline.types.log_options.LogOptions"]
    """<p>The options for a log driver.</p>"""
    parameters: NotRequired["aws_sdk_deadline.types.log_parameters.LogParameters"]
    """<p>The parameters for the log configuration.</p>"""
    error: NotRequired["aws_sdk_deadline.types.log_error.LogError"]
    """<p>The log configuration error details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfiguration) -> dict:
    out: dict = {}
    out["logDriver"] = value["log_driver"]
    if "options" in value:
        import aws_sdk_deadline.types.log_options

        out["options"] = aws_sdk_deadline.types.log_options.serialize_json(
            value["options"]
        )
    if "parameters" in value:
        import aws_sdk_deadline.types.log_parameters

        out["parameters"] = aws_sdk_deadline.types.log_parameters.serialize_json(
            value["parameters"]
        )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> LogConfiguration:
    out: LogConfiguration = {}  # type: ignore[typeddict-item]
    if "logDriver" in data:
        out["log_driver"] = data["logDriver"]
    else:
        raise DeserializationError("LogConfiguration.log_driver required")
    if "options" in data:
        import aws_sdk_deadline.types.log_options

        out["options"] = aws_sdk_deadline.types.log_options.deserialize_json(
            data["options"]
        )
    if "parameters" in data:
        import aws_sdk_deadline.types.log_parameters

        out["parameters"] = aws_sdk_deadline.types.log_parameters.deserialize_json(
            data["parameters"]
        )
    if "error" in data:
        out["error"] = data["error"]
    return out
