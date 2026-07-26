"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment


class CreateAssessmentResponse(TypedDict, closed=True):
    assessment: NotRequired["capo_auditmanager.types.assessment.Assessment"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentResponse) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.serialize_json(
            value["assessment"]
        )
    return out


def deserialize_json(data: dict) -> CreateAssessmentResponse:
    out: CreateAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "assessment" in data:
        import capo_auditmanager.types.assessment

        out["assessment"] = capo_auditmanager.types.assessment.deserialize_json(
            data["assessment"]
        )
    return out
