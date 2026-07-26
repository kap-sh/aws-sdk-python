"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_create_delegation_by_assessment_errors
    import capo_auditmanager.types.delegations


class BatchCreateDelegationByAssessmentResponse(TypedDict, closed=True):
    delegations: NotRequired["capo_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the assessment. </p>"""
    errors: NotRequired[
        "capo_auditmanager.types.batch_create_delegation_by_assessment_errors.BatchCreateDelegationByAssessmentErrors"
    ]
    """<p> A list of errors that the <code>BatchCreateDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentResponse) -> dict:
    out: dict = {}
    if "delegations" in value:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    if "errors" in value:
        import capo_auditmanager.types.batch_create_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_create_delegation_by_assessment_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateDelegationByAssessmentResponse:
    out: BatchCreateDelegationByAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "delegations" in data:
        import capo_auditmanager.types.delegations

        out["delegations"] = capo_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if "errors" in data:
        import capo_auditmanager.types.batch_create_delegation_by_assessment_errors

        out["errors"] = (
            capo_auditmanager.types.batch_create_delegation_by_assessment_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
