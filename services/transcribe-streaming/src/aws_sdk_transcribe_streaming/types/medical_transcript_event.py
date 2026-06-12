"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalTranscriptEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_transcript


class MedicalTranscriptEvent(TypedDict):
    transcript: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_transcript.MedicalTranscript"
    ]
    """<p>Contains <code>Results</code>, which contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalTranscriptEvent) -> dict:
    out: dict = {}
    if "transcript" in value:
        import aws_sdk_transcribe_streaming.types.medical_transcript

        out["Transcript"] = (
            aws_sdk_transcribe_streaming.types.medical_transcript.serialize_json(
                value["transcript"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalTranscriptEvent:
    out: MedicalTranscriptEvent = {}  # type: ignore[typeddict-item]
    if "Transcript" in data:
        import aws_sdk_transcribe_streaming.types.medical_transcript

        out["transcript"] = (
            aws_sdk_transcribe_streaming.types.medical_transcript.deserialize_json(
                data["Transcript"]
            )
        )
    return out
