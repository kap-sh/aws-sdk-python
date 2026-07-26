"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.non_empty_string256


class GetSpeakerSearchTaskRequest(TypedDict, closed=True):
    voice_connector_id: (
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    speaker_search_task_id: (
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the speaker search task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSpeakerSearchTaskRequest:
    out: GetSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    return out
