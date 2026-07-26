"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string256


class GetVoiceProfileRequest(TypedDict, closed=True):
    voice_profile_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    """<p>The voice profile ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceProfileRequest:
    out: GetVoiceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
