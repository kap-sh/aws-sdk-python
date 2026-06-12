"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribePostStreamAnalyticsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.clinical_note_generation_result


class MedicalScribePostStreamAnalyticsResult(TypedDict):
    clinical_note_generation_result: NotRequired[
        "aws_sdk_transcribe_streaming.types.clinical_note_generation_result.ClinicalNoteGenerationResult"
    ]
    """<p>Provides the Clinical Note Generation result for post-stream analytics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamAnalyticsResult) -> dict:
    out: dict = {}
    if "clinical_note_generation_result" in value:
        import aws_sdk_transcribe_streaming.types.clinical_note_generation_result

        out["ClinicalNoteGenerationResult"] = (
            aws_sdk_transcribe_streaming.types.clinical_note_generation_result.serialize_json(
                value["clinical_note_generation_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamAnalyticsResult:
    out: MedicalScribePostStreamAnalyticsResult = {}  # type: ignore[typeddict-item]
    if "ClinicalNoteGenerationResult" in data:
        import aws_sdk_transcribe_streaming.types.clinical_note_generation_result

        out["clinical_note_generation_result"] = (
            aws_sdk_transcribe_streaming.types.clinical_note_generation_result.deserialize_json(
                data["ClinicalNoteGenerationResult"]
            )
        )
    return out
