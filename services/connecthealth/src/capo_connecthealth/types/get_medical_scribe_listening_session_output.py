"""Generated from Smithy shape ``com.amazonaws.connecthealth#GetMedicalScribeListeningSessionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_scribe_listening_session_details


class GetMedicalScribeListeningSessionOutput(TypedDict, closed=True):
    medical_scribe_listening_session_details: NotRequired[
        "capo_connecthealth.types.medical_scribe_listening_session_details.MedicalScribeListeningSessionDetails"
    ]
    """<p>Details about the Medical Scribe listening session</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeListeningSessionOutput) -> dict:
    out: dict = {}
    if "medical_scribe_listening_session_details" in value:
        import capo_connecthealth.types.medical_scribe_listening_session_details

        out["medicalScribeListeningSessionDetails"] = (
            capo_connecthealth.types.medical_scribe_listening_session_details.serialize_json(
                value["medical_scribe_listening_session_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMedicalScribeListeningSessionOutput:
    out: GetMedicalScribeListeningSessionOutput = {}  # type: ignore[typeddict-item]
    if "medicalScribeListeningSessionDetails" in data:
        import capo_connecthealth.types.medical_scribe_listening_session_details

        out["medical_scribe_listening_session_details"] = (
            capo_connecthealth.types.medical_scribe_listening_session_details.deserialize_json(
                data["medicalScribeListeningSessionDetails"]
            )
        )
    return out
