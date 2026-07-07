"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceProfileDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string256
    import aws_sdk_chime_sdk_voice.types.voice_profile_domain_description
    import aws_sdk_chime_sdk_voice.types.voice_profile_domain_name


class UpdateVoiceProfileDomainRequest(TypedDict, closed=True):
    voice_profile_domain_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The domain ID.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile_domain_name.VoiceProfileDomainName"
    ]
    """<p>The name of the voice profile domain.</p>"""
    description: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile_domain_description.VoiceProfileDomainDescription"
    ]
    """<p>The description of the voice profile domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceProfileDomainRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateVoiceProfileDomainRequest:
    out: UpdateVoiceProfileDomainRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
