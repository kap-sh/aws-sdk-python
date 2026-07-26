"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#StartMeetingTranscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.guid_string
    import capo_chime_sdk_meetings.types.transcription_configuration


class StartMeetingTranscriptionRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The unique ID of the meeting being transcribed.</p>"""
    transcription_configuration: "capo_chime_sdk_meetings.types.transcription_configuration.TranscriptionConfiguration"
    """<p>The configuration for the current transcription operation. Must contain <code>EngineTranscribeSettings</code> or <code>EngineTranscribeMedicalSettings</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartMeetingTranscriptionRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.transcription_configuration

    out["TranscriptionConfiguration"] = (
        capo_chime_sdk_meetings.types.transcription_configuration.serialize_json(
            value["transcription_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartMeetingTranscriptionRequest:
    out: StartMeetingTranscriptionRequest = {}  # type: ignore[typeddict-item]
    if "TranscriptionConfiguration" in data:
        import capo_chime_sdk_meetings.types.transcription_configuration

        out["transcription_configuration"] = (
            capo_chime_sdk_meetings.types.transcription_configuration.deserialize_json(
                data["TranscriptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartMeetingTranscriptionRequest.transcription_configuration required"
        )
    return out
