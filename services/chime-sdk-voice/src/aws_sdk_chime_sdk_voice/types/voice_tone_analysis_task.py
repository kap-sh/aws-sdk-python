"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceToneAnalysisTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.call_details
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.non_empty_string256
    import aws_sdk_chime_sdk_voice.types.string


class VoiceToneAnalysisTask(TypedDict, closed=True):
    voice_tone_analysis_task_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The ID of the voice tone analysis task.</p>"""
    voice_tone_analysis_task_status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of a voice tone analysis task, <code>IN_QUEUE</code>, <code>IN_PROGRESS</code>, <code>PARTIAL_SUCCESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, or <code>STOPPED</code>.</p>"""
    call_details: NotRequired["aws_sdk_chime_sdk_voice.types.call_details.CallDetails"]
    """<p>The call details of a voice tone analysis task.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice tone analysis task was created.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice tone analysis task was updated.</p>"""
    started_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a voice tone analysis task started.</p>"""
    status_message: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The status of a voice tone analysis task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceToneAnalysisTask) -> dict:
    out: dict = {}
    if "voice_tone_analysis_task_id" in value:
        out["VoiceToneAnalysisTaskId"] = value["voice_tone_analysis_task_id"]
    if "voice_tone_analysis_task_status" in value:
        out["VoiceToneAnalysisTaskStatus"] = value["voice_tone_analysis_task_status"]
    if "call_details" in value:
        import aws_sdk_chime_sdk_voice.types.call_details

        out["CallDetails"] = aws_sdk_chime_sdk_voice.types.call_details.serialize_json(
            value["call_details"]
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "started_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["StartedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["started_timestamp"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> VoiceToneAnalysisTask:
    out: VoiceToneAnalysisTask = {}  # type: ignore[typeddict-item]
    if "VoiceToneAnalysisTaskId" in data:
        out["voice_tone_analysis_task_id"] = data["VoiceToneAnalysisTaskId"]
    if "VoiceToneAnalysisTaskStatus" in data:
        out["voice_tone_analysis_task_status"] = data["VoiceToneAnalysisTaskStatus"]
    if "CallDetails" in data:
        import aws_sdk_chime_sdk_voice.types.call_details

        out["call_details"] = (
            aws_sdk_chime_sdk_voice.types.call_details.deserialize_json(
                data["CallDetails"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "StartedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["started_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["StartedTimestamp"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
