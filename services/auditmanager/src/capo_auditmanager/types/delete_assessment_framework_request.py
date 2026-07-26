"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.uuid


class DeleteAssessmentFrameworkRequest(TypedDict, closed=True):
    framework_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The identifier for the custom framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentFrameworkRequest:
    out: DeleteAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    return out
