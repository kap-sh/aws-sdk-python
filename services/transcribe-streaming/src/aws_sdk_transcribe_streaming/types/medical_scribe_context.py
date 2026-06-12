"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_patient_context


class MedicalScribeContext(TypedDict):
    patient_context: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_patient_context.MedicalScribePatientContext"
    ]
    """<p>Contains patient-specific information used to customize the clinical note generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeContext) -> dict:
    out: dict = {}
    if "patient_context" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_patient_context

        out["PatientContext"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_patient_context.serialize_json(
                value["patient_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeContext:
    out: MedicalScribeContext = {}  # type: ignore[typeddict-item]
    if "PatientContext" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_patient_context

        out["patient_context"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_patient_context.deserialize_json(
                data["PatientContext"]
            )
        )
    return out
