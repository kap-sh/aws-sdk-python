"""Generated from Smithy shape ``com.amazonaws.amp#LoggingConfigurationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.logging_configuration_status_code


class LoggingConfigurationStatus(TypedDict):
    status_code: "aws_sdk_amp.types.logging_configuration_status_code.LoggingConfigurationStatusCode"
    """<p>The current status of the current rules and alerting logging configuration.</p> <note> <p>These logging configurations are only for rules and alerting logs.</p> </note>"""
    status_reason: NotRequired["str"]
    """<p>If failed, the reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> LoggingConfigurationStatus:
    out: LoggingConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError("LoggingConfigurationStatus.status_code required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
