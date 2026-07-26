"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.non_empty_string


class GetVoiceToneAnalysisTaskRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier of the resource to be updated. Valid values include the ID and ARN of the media insights pipeline.</p>"""
    voice_tone_analysis_task_id: (
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    )
    """<p>The ID of the voice tone analysis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVoiceToneAnalysisTaskRequest:
    out: GetVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    return out
