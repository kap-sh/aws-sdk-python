"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StopSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class StopSpeakerSearchTaskRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    speaker_search_task_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The speaker search task ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSpeakerSearchTaskRequest:
    out: StopSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    return out
