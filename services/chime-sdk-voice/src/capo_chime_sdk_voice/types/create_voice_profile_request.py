"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string256


class CreateVoiceProfileRequest(TypedDict, closed=True):
    speaker_search_task_id: (
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceProfileRequest) -> dict:
    out: dict = {}
    out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    return out


def deserialize_json(data: dict) -> CreateVoiceProfileRequest:
    out: CreateVoiceProfileRequest = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchTaskId" in data:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    else:
        raise DeserializationError(
            "CreateVoiceProfileRequest.speaker_search_task_id required"
        )
    return out
