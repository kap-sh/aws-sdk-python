"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StopVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class StopVoiceToneAnalysisTaskRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    voice_tone_analysis_task_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the voice tone analysis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopVoiceToneAnalysisTaskRequest:
    out: StopVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    return out
