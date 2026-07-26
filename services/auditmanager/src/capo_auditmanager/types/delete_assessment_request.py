"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.uuid


class DeleteAssessmentRequest(TypedDict, closed=True):
    assessment_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentRequest:
    out: DeleteAssessmentRequest = {}  # type: ignore[typeddict-item]
    return out
