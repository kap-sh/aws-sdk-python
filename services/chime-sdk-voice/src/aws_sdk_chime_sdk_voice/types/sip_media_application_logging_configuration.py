"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean


class SipMediaApplicationLoggingConfiguration(TypedDict, closed=True):
    enable_sip_media_application_message_logs: NotRequired[
        "aws_sdk_chime_sdk_voice.types.boolean.Boolean"
    ]
    """<p>Enables message logging for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationLoggingConfiguration) -> dict:
    out: dict = {}
    if "enable_sip_media_application_message_logs" in value:
        out["EnableSipMediaApplicationMessageLogs"] = value[
            "enable_sip_media_application_message_logs"
        ]
    return out


def deserialize_json(data: dict) -> SipMediaApplicationLoggingConfiguration:
    out: SipMediaApplicationLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableSipMediaApplicationMessageLogs" in data:
        out["enable_sip_media_application_message_logs"] = data[
            "EnableSipMediaApplicationMessageLogs"
        ]
    return out
