"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipMediaApplicationAlexaSkillConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.alexa_skill_id_list
    import aws_sdk_chime_sdk_voice.types.alexa_skill_status


class SipMediaApplicationAlexaSkillConfiguration(TypedDict, closed=True):
    alexa_skill_status: (
        "aws_sdk_chime_sdk_voice.types.alexa_skill_status.AlexaSkillStatus"
    )
    """<p>The status of the Alexa Skill configuration.</p>"""
    alexa_skill_ids: (
        "aws_sdk_chime_sdk_voice.types.alexa_skill_id_list.AlexaSkillIdList"
    )
    """<p>The ID of the Alexa Skill configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipMediaApplicationAlexaSkillConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.alexa_skill_status

    out["AlexaSkillStatus"] = (
        aws_sdk_chime_sdk_voice.types.alexa_skill_status.serialize_json(
            value["alexa_skill_status"]
        )
    )
    import aws_sdk_chime_sdk_voice.types.alexa_skill_id_list

    out["AlexaSkillIds"] = (
        aws_sdk_chime_sdk_voice.types.alexa_skill_id_list.serialize_json(
            value["alexa_skill_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> SipMediaApplicationAlexaSkillConfiguration:
    out: SipMediaApplicationAlexaSkillConfiguration = {}  # type: ignore[typeddict-item]
    if "AlexaSkillStatus" in data:
        import aws_sdk_chime_sdk_voice.types.alexa_skill_status

        out["alexa_skill_status"] = (
            aws_sdk_chime_sdk_voice.types.alexa_skill_status.deserialize_json(
                data["AlexaSkillStatus"]
            )
        )
    else:
        raise DeserializationError(
            "SipMediaApplicationAlexaSkillConfiguration.alexa_skill_status required"
        )
    if "AlexaSkillIds" in data:
        import aws_sdk_chime_sdk_voice.types.alexa_skill_id_list

        out["alexa_skill_ids"] = (
            aws_sdk_chime_sdk_voice.types.alexa_skill_id_list.deserialize_json(
                data["AlexaSkillIds"]
            )
        )
    else:
        raise DeserializationError(
            "SipMediaApplicationAlexaSkillConfiguration.alexa_skill_ids required"
        )
    return out
