"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutSipMediaApplicationLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sip_media_application_logging_configuration


class PutSipMediaApplicationLoggingConfigurationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""
    sip_media_application_logging_configuration: NotRequired[
        "capo_chime_sdk_voice.types.sip_media_application_logging_configuration.SipMediaApplicationLoggingConfiguration"
    ]
    """<p>The logging configuration for the specified SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSipMediaApplicationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "sip_media_application_logging_configuration" in value:
        import capo_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["SipMediaApplicationLoggingConfiguration"] = (
            capo_chime_sdk_voice.types.sip_media_application_logging_configuration.serialize_json(
                value["sip_media_application_logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutSipMediaApplicationLoggingConfigurationRequest:
    out: PutSipMediaApplicationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationLoggingConfiguration" in data:
        import capo_chime_sdk_voice.types.sip_media_application_logging_configuration

        out["sip_media_application_logging_configuration"] = (
            capo_chime_sdk_voice.types.sip_media_application_logging_configuration.deserialize_json(
                data["SipMediaApplicationLoggingConfiguration"]
            )
        )
    return out
