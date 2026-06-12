"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.boolean
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.non_empty_string256


class GetVoiceToneAnalysisTaskRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    voice_tone_analysis_task_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the voice tone analysis task.</p>"""
    is_caller: "aws_sdk_chime_sdk_voice.types.boolean.Boolean"
    """<p>Specifies whether the voice being analyzed is the caller (originator) or the callee (responder).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceToneAnalysisTaskRequest:
    out: GetVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    return out
