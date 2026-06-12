"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_profile


class CreateVoiceProfileResponse(TypedDict):
    voice_profile: NotRequired[
        "aws_sdk_chime_sdk_voice.types.voice_profile.VoiceProfile"
    ]
    """<p>The requested voice profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceProfileResponse) -> dict:
    out: dict = {}
    if "voice_profile" in value:
        import aws_sdk_chime_sdk_voice.types.voice_profile

        out["VoiceProfile"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile.serialize_json(
                value["voice_profile"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceProfileResponse:
    out: CreateVoiceProfileResponse = {}  # type: ignore[typeddict-item]
    if "VoiceProfile" in data:
        import aws_sdk_chime_sdk_voice.types.voice_profile

        out["voice_profile"] = (
            aws_sdk_chime_sdk_voice.types.voice_profile.deserialize_json(
                data["VoiceProfile"]
            )
        )
    return out
