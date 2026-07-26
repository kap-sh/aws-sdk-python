"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceToneAnalysisTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status


class VoiceToneAnalysisTask(TypedDict, closed=True):
    voice_tone_analysis_task_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the voice tone analysis task.</p>"""
    voice_tone_analysis_task_status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.MediaPipelineTaskStatus"
    ]
    """<p>The status of a voice tone analysis task.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice tone analysis task was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice tone analysis task was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceToneAnalysisTask) -> dict:
    out: dict = {}
    if "voice_tone_analysis_task_id" in value:
        out["VoiceToneAnalysisTaskId"] = value["voice_tone_analysis_task_id"]
    if "voice_tone_analysis_task_status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status

        out["VoiceToneAnalysisTaskStatus"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.serialize_json(
                value["voice_tone_analysis_task_status"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> VoiceToneAnalysisTask:
    out: VoiceToneAnalysisTask = {}  # type: ignore[typeddict-item]
    if "VoiceToneAnalysisTaskId" in data:
        out["voice_tone_analysis_task_id"] = data["VoiceToneAnalysisTaskId"]
    if "VoiceToneAnalysisTaskStatus" in data:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status

        out["voice_tone_analysis_task_status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.deserialize_json(
                data["VoiceToneAnalysisTaskStatus"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out
