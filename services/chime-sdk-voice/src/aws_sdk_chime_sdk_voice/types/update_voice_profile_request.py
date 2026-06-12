"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class UpdateVoiceProfileRequest(TypedDict):
    voice_profile_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The profile ID.</p>"""
    speaker_search_task_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceProfileRequest) -> dict:
    out: dict = {}
    out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    return out


def deserialize_json(data: dict) -> UpdateVoiceProfileRequest:
    out: UpdateVoiceProfileRequest = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchTaskId" in data:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    else:
        raise DeserializationError(
            "UpdateVoiceProfileRequest.speaker_search_task_id required"
        )
    return out
