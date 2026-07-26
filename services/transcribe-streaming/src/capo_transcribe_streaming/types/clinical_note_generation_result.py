"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ClinicalNoteGenerationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.clinical_note_generation_status
    import capo_transcribe_streaming.types.string
    import capo_transcribe_streaming.types.uri


class ClinicalNoteGenerationResult(TypedDict, closed=True):
    clinical_note_output_location: NotRequired[
        "capo_transcribe_streaming.types.uri.Uri"
    ]
    """<p>Holds the Amazon S3 URI for the output Clinical Note. </p>"""
    transcript_output_location: NotRequired["capo_transcribe_streaming.types.uri.Uri"]
    """<p>Holds the Amazon S3 URI for the output Transcript. </p>"""
    status: NotRequired[
        "capo_transcribe_streaming.types.clinical_note_generation_status.ClinicalNoteGenerationStatus"
    ]
    """<p>The status of the clinical note generation.</p> <p>Possible Values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> </ul> <p> After audio streaming finishes, and you send a <code>MedicalScribeSessionControlEvent</code> event (with END_OF_SESSION as the Type), the status is set to <code>IN_PROGRESS</code>. If the status is <code>COMPLETED</code>, the analytics completed successfully, and you can find the results at the locations specified in <code>ClinicalNoteOutputLocation</code> and <code>TranscriptOutputLocation</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details about the failure. </p>"""
    failure_reason: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>If <code>ClinicalNoteGenerationResult</code> is <code>FAILED</code>, information about why it failed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationResult) -> dict:
    out: dict = {}
    if "clinical_note_output_location" in value:
        out["ClinicalNoteOutputLocation"] = value["clinical_note_output_location"]
    if "transcript_output_location" in value:
        out["TranscriptOutputLocation"] = value["transcript_output_location"]
    if "status" in value:
        import capo_transcribe_streaming.types.clinical_note_generation_status

        out["Status"] = (
            capo_transcribe_streaming.types.clinical_note_generation_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationResult:
    out: ClinicalNoteGenerationResult = {}  # type: ignore[typeddict-item]
    if "ClinicalNoteOutputLocation" in data:
        out["clinical_note_output_location"] = data["ClinicalNoteOutputLocation"]
    if "TranscriptOutputLocation" in data:
        out["transcript_output_location"] = data["TranscriptOutputLocation"]
    if "Status" in data:
        import capo_transcribe_streaming.types.clinical_note_generation_status

        out["status"] = (
            capo_transcribe_streaming.types.clinical_note_generation_status.deserialize_json(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
