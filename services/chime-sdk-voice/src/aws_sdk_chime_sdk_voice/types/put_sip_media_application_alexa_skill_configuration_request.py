"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutSipMediaApplicationAlexaSkillConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration


class PutSipMediaApplicationAlexaSkillConfigurationRequest(TypedDict):
    sip_media_application_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""
    sip_media_application_alexa_skill_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.SipMediaApplicationAlexaSkillConfiguration"
    ]
    """<p>The Alexa Skill configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSipMediaApplicationAlexaSkillConfigurationRequest) -> dict:
    out: dict = {}
    if "sip_media_application_alexa_skill_configuration" in value:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration

        out["SipMediaApplicationAlexaSkillConfiguration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.serialize_json(
                value["sip_media_application_alexa_skill_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> PutSipMediaApplicationAlexaSkillConfigurationRequest:
    out: PutSipMediaApplicationAlexaSkillConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationAlexaSkillConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration

        out["sip_media_application_alexa_skill_configuration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.deserialize_json(
                data["SipMediaApplicationAlexaSkillConfiguration"]
            )
        )
    return out
