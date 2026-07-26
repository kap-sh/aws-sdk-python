"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SpeakerSearchTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status


class SpeakerSearchTask(TypedDict, closed=True):
    speaker_search_task_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The speaker search task ID.</p>"""
    speaker_search_task_status: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.MediaPipelineTaskStatus"
    ]
    """<p>The status of the speaker search task.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchTask) -> dict:
    out: dict = {}
    if "speaker_search_task_id" in value:
        out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    if "speaker_search_task_status" in value:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status

        out["SpeakerSearchTaskStatus"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.serialize_json(
                value["speaker_search_task_status"]
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


def deserialize_json(data: dict) -> SpeakerSearchTask:
    out: SpeakerSearchTask = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchTaskId" in data:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    if "SpeakerSearchTaskStatus" in data:
        import capo_chime_sdk_media_pipelines.types.media_pipeline_task_status

        out["speaker_search_task_status"] = (
            capo_chime_sdk_media_pipelines.types.media_pipeline_task_status.deserialize_json(
                data["SpeakerSearchTaskStatus"]
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
