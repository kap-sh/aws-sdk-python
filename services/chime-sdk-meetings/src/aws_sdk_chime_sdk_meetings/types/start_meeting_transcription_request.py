"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#StartMeetingTranscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string
    import aws_sdk_chime_sdk_meetings.types.transcription_configuration


class StartMeetingTranscriptionRequest(TypedDict):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The unique ID of the meeting being transcribed.</p>"""
    transcription_configuration: "aws_sdk_chime_sdk_meetings.types.transcription_configuration.TranscriptionConfiguration"
    """<p>The configuration for the current transcription operation. Must contain <code>EngineTranscribeSettings</code> or <code>EngineTranscribeMedicalSettings</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMeetingTranscriptionRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_meetings.types.transcription_configuration

    out["TranscriptionConfiguration"] = (
        aws_sdk_chime_sdk_meetings.types.transcription_configuration.serialize_json(
            value["transcription_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartMeetingTranscriptionRequest:
    out: StartMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
    if "TranscriptionConfiguration" in data:
        import aws_sdk_chime_sdk_meetings.types.transcription_configuration

        out["transcription_configuration"] = (
            aws_sdk_chime_sdk_meetings.types.transcription_configuration.deserialize_json(
                data["TranscriptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartMeetingTranscriptionRequest.transcription_configuration required"
        )
    return out
