"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.clinical_note_generation_result


class MedicalScribePostStreamActionsResult(TypedDict, closed=True):
    clinical_note_generation_result: NotRequired[
        "capo_connecthealth.types.clinical_note_generation_result.ClinicalNoteGenerationResult"
    ]
    """<p>Results of clinical note generation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionsResult) -> dict:
    out: dict = {}
    if "clinical_note_generation_result" in value:
        import capo_connecthealth.types.clinical_note_generation_result

        out["clinicalNoteGenerationResult"] = (
            capo_connecthealth.types.clinical_note_generation_result.serialize_json(
                value["clinical_note_generation_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionsResult:
    out: MedicalScribePostStreamActionsResult = {}  # type: ignore[typeddict-item]
    if "clinicalNoteGenerationResult" in data:
        import capo_connecthealth.types.clinical_note_generation_result

        out["clinical_note_generation_result"] = (
            capo_connecthealth.types.clinical_note_generation_result.deserialize_json(
                data["clinicalNoteGenerationResult"]
            )
        )
    return out
