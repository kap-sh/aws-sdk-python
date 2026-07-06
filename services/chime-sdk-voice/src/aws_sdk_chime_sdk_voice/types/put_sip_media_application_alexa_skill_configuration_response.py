"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutSipMediaApplicationAlexaSkillConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration


class PutSipMediaApplicationAlexaSkillConfigurationResponse(TypedDict, closed=True):
    sip_media_application_alexa_skill_configuration: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.SipMediaApplicationAlexaSkillConfiguration"
    ]
    """<p>Returns the Alexa Skill configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PutSipMediaApplicationAlexaSkillConfigurationResponse,
) -> dict:
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
) -> PutSipMediaApplicationAlexaSkillConfigurationResponse:
    out: PutSipMediaApplicationAlexaSkillConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationAlexaSkillConfiguration" in data:
        import aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration

        out["sip_media_application_alexa_skill_configuration"] = (
            aws_sdk_chime_sdk_voice.types.sip_media_application_alexa_skill_configuration.deserialize_json(
                data["SipMediaApplicationAlexaSkillConfiguration"]
            )
        )
    return out
