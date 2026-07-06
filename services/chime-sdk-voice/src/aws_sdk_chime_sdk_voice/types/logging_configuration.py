"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean


class LoggingConfiguration(TypedDict, closed=True):
    enable_sip_logs: NotRequired["aws_sdk_chime_sdk_voice.types.boolean.Boolean"]
    """<p>Boolean that enables sending SIP message logs to Amazon CloudWatch.</p>"""
    enable_media_metric_logs: NotRequired[
        "aws_sdk_chime_sdk_voice.types.boolean.Boolean"
    ]
    """<p>Enables or disables media metrics logging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfiguration) -> dict:
    out: dict = {}
    if "enable_sip_logs" in value:
        out["EnableSIPLogs"] = value["enable_sip_logs"]
    if "enable_media_metric_logs" in value:
        out["EnableMediaMetricLogs"] = value["enable_media_metric_logs"]
    return out


def deserialize_json(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableSIPLogs" in data:
        out["enable_sip_logs"] = data["EnableSIPLogs"]
    if "EnableMediaMetricLogs" in data:
        out["enable_media_metric_logs"] = data["EnableMediaMetricLogs"]
    return out
