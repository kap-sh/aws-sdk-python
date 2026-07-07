"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipMediaApplicationAlexaSkillConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetSipMediaApplicationAlexaSkillConfigurationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipMediaApplicationAlexaSkillConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetSipMediaApplicationAlexaSkillConfigurationRequest:
    out: GetSipMediaApplicationAlexaSkillConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
