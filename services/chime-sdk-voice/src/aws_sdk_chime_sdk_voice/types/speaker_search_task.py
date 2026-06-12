"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.call_details
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.non_empty_string256
    import aws_sdk_chime_sdk_voice.types.speaker_search_details
    import aws_sdk_chime_sdk_voice.types.string


class SpeakerSearchTask(TypedDict):
    speaker_search_task_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    ]
    """<p>The speaker search task ID.</p>"""
    speaker_search_task_status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the speaker search task, <code>IN_QUEUE</code>, <code>IN_PROGRESS</code>, <code>PARTIAL_SUCCESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, or <code>STOPPED</code>.</p>"""
    call_details: NotRequired["aws_sdk_chime_sdk_voice.types.call_details.CallDetails"]
    """<p>The call details of a speaker search task.</p>"""
    speaker_search_details: NotRequired[
        "aws_sdk_chime_sdk_voice.types.speaker_search_details.SpeakerSearchDetails"
    ]
    """<p>The details of a speaker search task.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was created.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which a speaker search task was updated.</p>"""
    started_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the speaker search task began.</p>"""
    status_message: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>A detailed message about the status of a speaker search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchTask) -> dict:
    out: dict = {}
    if "speaker_search_task_id" in value:
        out["SpeakerSearchTaskId"] = value["speaker_search_task_id"]
    if "speaker_search_task_status" in value:
        out["SpeakerSearchTaskStatus"] = value["speaker_search_task_status"]
    if "call_details" in value:
        import aws_sdk_chime_sdk_voice.types.call_details

        out["CallDetails"] = aws_sdk_chime_sdk_voice.types.call_details.serialize_json(
            value["call_details"]
        )
    if "speaker_search_details" in value:
        import aws_sdk_chime_sdk_voice.types.speaker_search_details

        out["SpeakerSearchDetails"] = (
            aws_sdk_chime_sdk_voice.types.speaker_search_details.serialize_json(
                value["speaker_search_details"]
            )
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


def deserialize_json(data: dict) -> SpeakerSearchTask:
    out: SpeakerSearchTask = {}  # type: ignore[typeddict-item]
    if "SpeakerSearchTaskId" in data:
        out["speaker_search_task_id"] = data["SpeakerSearchTaskId"]
    if "SpeakerSearchTaskStatus" in data:
        out["speaker_search_task_status"] = data["SpeakerSearchTaskStatus"]
    if "CallDetails" in data:
        import aws_sdk_chime_sdk_voice.types.call_details

        out["call_details"] = (
            aws_sdk_chime_sdk_voice.types.call_details.deserialize_json(
                data["CallDetails"]
            )
        )
    if "SpeakerSearchDetails" in data:
        import aws_sdk_chime_sdk_voice.types.speaker_search_details

        out["speaker_search_details"] = (
            aws_sdk_chime_sdk_voice.types.speaker_search_details.deserialize_json(
                data["SpeakerSearchDetails"]
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
