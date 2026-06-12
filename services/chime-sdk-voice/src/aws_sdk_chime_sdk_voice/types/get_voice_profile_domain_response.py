"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceProfileDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_profile_domain


class GetVoiceProfileDomainResponse(TypedDict):
    voice_profile_domain: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile_domain.VoiceProfileDomain"
    ]
    """<p>The details of the voice profile domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceProfileDomainResponse) -> dict:
    out: dict = {}
    if "voice_profile_domain" in value:
        import aws_sdk_chime_sdk_voice.types.voice_profile_domain

        out["VoiceProfileDomain"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_domain.serialize_json(
                value["voice_profile_domain"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetVoiceProfileDomainResponse:
    out: GetVoiceProfileDomainResponse = {}  # type: ignore[typeddict-item]
    if "VoiceProfileDomain" in data:
        import aws_sdk_chime_sdk_voice.types.voice_profile_domain

        out["voice_profile_domain"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile_domain.deserialize_json(
                data["VoiceProfileDomain"]
            )
        )
    return out
