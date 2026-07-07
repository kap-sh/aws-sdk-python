"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutSipMediaApplicationLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration


class PutSipMediaApplicationLoggingConfigurationResponse(TypedDict, closed=True):
    sip_media_application_logging_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.SipMediaApplicationLoggingConfiguration"
    ]
    """<p>The updated logging configuration for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSipMediaApplicationLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "sip_media_application_logging_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["SipMediaApplicationLoggingConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.serialize_json(
                value["sip_media_application_logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSipMediaApplicationLoggingConfigurationResponse:
    out: PutSipMediaApplicationLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationLoggingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["sip_media_application_logging_configuration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.deserialize_json(
                data["SipMediaApplicationLoggingConfiguration"]
            )
        )
    return out
