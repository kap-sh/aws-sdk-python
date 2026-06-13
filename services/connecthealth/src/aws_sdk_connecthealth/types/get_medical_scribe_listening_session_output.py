"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalScribeListeningSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_listening_session_details


class GetMedicalScribeListeningSessionOutput(TypedDict):
    medical_scribe_listening_session_details: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_listening_session_details.MedicalScribeListeningSessionDetails"
    ]
    """<p>Details about the Medical Scribe listening session</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeListeningSessionOutput) -> dict:
    out: dict = {}
    if "medical_scribe_listening_session_details" in value:
        import aws_sdk_connecthealth.types.medical_scribe_listening_session_details

        out["medicalScribeListeningSessionDetails"] = (
            aws_sdk_connecthealth.types.medical_scribe_listening_session_details.serialize_json(
                value["medical_scribe_listening_session_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMedicalScribeListeningSessionOutput:
    out: GetMedicalScribeListeningSessionOutput = {}  # type: ignore[typeddict-item]
    if "medicalScribeListeningSessionDetails" in data:
        import aws_sdk_connecthealth.types.medical_scribe_listening_session_details

        out["medical_scribe_listening_session_details"] = (
            aws_sdk_connecthealth.types.medical_scribe_listening_session_details.deserialize_json(
                data["medicalScribeListeningSessionDetails"]
            )
        )
    return out
