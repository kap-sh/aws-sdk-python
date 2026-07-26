"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_profile


class GetVoiceProfileResponse(TypedDict, closed=True):
    voice_profile: NotRequired["capo_chime_sdk_voice.types.voice_profile.VoiceProfile"]
    """<p>The voice profile details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceProfileResponse) -> dict:
    out: dict = {}
    if "voice_profile" in value:
        import capo_chime_sdk_voice.types.voice_profile

        out["VoiceProfile"] = capo_chime_sdk_voice.types.voice_profile.serialize_json(
            value["voice_profile"]
        )
    return out


def deserialize_json(data: dict) -> GetVoiceProfileResponse:
    out: GetVoiceProfileResponse = {}  # type: ignore[typeddict-item]
    if "VoiceProfile" in data:
        import capo_chime_sdk_voice.types.voice_profile

        out["voice_profile"] = (
            capo_chime_sdk_voice.types.voice_profile.deserialize_json(
                data["VoiceProfile"]
            )
        )
    return out
