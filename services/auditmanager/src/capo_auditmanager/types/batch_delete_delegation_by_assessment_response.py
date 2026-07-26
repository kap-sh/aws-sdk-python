"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors


class BatchDeleteDelegationByAssessmentResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.BatchDeleteDelegationByAssessmentErrors"
    ]
    """<p> A list of errors that the <code>BatchDeleteDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteDelegationByAssessmentResponse:
    out: BatchDeleteDelegationByAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_auditmanager.types.batch_delete_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_delete_delegation_by_assessment_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
