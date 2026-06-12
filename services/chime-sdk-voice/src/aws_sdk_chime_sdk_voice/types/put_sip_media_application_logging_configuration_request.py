"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutSipMediaApplicationLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration


class PutSipMediaApplicationLoggingConfigurationRequest(TypedDict):
    sip_media_application_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""
    sip_media_application_logging_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.SipMediaApplicationLoggingConfiguration"
    ]
    """<p>The logging configuration for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSipMediaApplicationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "sip_media_application_logging_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["SipMediaApplicationLoggingConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.serialize_json(
                value["sip_media_application_logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSipMediaApplicationLoggingConfigurationRequest:
    out: PutSipMediaApplicationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationLoggingConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["sip_media_application_logging_configuration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_logging_configuration.deserialize_json(
                data["SipMediaApplicationLoggingConfiguration"]
            )
        )
    return out
