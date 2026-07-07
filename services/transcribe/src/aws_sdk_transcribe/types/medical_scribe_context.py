"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.medical_scribe_patient_context


class MedicalScribeContext(TypedDict, closed=True):
    patient_context: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_patient_context.MedicalScribePatientContext"
    ]
    """<p>Contains patient-specific information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeContext) -> dict:
    out: dict = {}
    if "patient_context" in value:
        import aws_sdk_transcribe.types.medical_scribe_patient_context

        out["PatientContext"] = (
            aws_sdk_transcribe.types.medical_scribe_patient_context.serialize_aws_json_1_1(
                value["patient_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeContext:
    out: MedicalScribeContext = {}  # type: ignore[typeddict-item]
    if "PatientContext" in data:
        import aws_sdk_transcribe.types.medical_scribe_patient_context

        out["patient_context"] = (
            aws_sdk_transcribe.types.medical_scribe_patient_context.deserialize_aws_json_1_1(
                data["PatientContext"]
            )
        )
    return out
