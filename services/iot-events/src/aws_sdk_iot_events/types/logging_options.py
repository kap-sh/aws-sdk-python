"""Generated from Smithy shape ``com.amazonaws.iotevents#LoggingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.detector_debug_options
    import aws_sdk_iot_events.types.logging_enabled
    import aws_sdk_iot_events.types.logging_level


class LoggingOptions(TypedDict, closed=True):
    role_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform logging.</p>"""
    level: "aws_sdk_iot_events.types.logging_level.LoggingLevel"
    """<p>The logging level.</p>"""
    enabled: "aws_sdk_iot_events.types.logging_enabled.LoggingEnabled"
    """<p>If TRUE, logging is enabled for AWS IoT Events.</p>"""
    detector_debug_options: NotRequired[
        "aws_sdk_iot_events.types.detector_debug_options.DetectorDebugOptions"
    ]
    """<p>Information that identifies those detector models and their detectors (instances) for which the logging level is given.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingOptions) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import aws_sdk_iot_events.types.logging_level

    out["level"] = aws_sdk_iot_events.types.logging_level.serialize_json(value["level"])
    out["enabled"] = value.get("enabled", False)
    if "detector_debug_options" in value:
        import aws_sdk_iot_events.types.detector_debug_options

        out["detectorDebugOptions"] = (
            aws_sdk_iot_events.types.detector_debug_options.serialize_json(
                value["detector_debug_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingOptions:
    out: LoggingOptions = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("LoggingOptions.role_arn required")
    if "level" in data:
        import aws_sdk_iot_events.types.logging_level

        out["level"] = aws_sdk_iot_events.types.logging_level.deserialize_json(
            data["level"]
        )
    else:
        raise DeserializationError("LoggingOptions.level required")
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "detectorDebugOptions" in data:
        import aws_sdk_iot_events.types.detector_debug_options

        out["detector_debug_options"] = (
            aws_sdk_iot_events.types.detector_debug_options.deserialize_json(
                data["detectorDebugOptions"]
            )
        )
    return out
