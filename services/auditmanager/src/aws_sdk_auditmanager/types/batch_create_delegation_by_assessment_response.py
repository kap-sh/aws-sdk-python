"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors
    import aws_sdk_auditmanager.types.delegations


class BatchCreateDelegationByAssessmentResponse(TypedDict):
    delegations: NotRequired["aws_sdk_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the assessment. </p>"""
    errors: NotRequired[
        "aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors.BatchCreateDelegationByAssessmentErrors"
    ]
    """<p> A list of errors that the <code>BatchCreateDelegationByAssessment</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentResponse) -> dict:
    out: dict = {}
    if "delegations" in value:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    if "errors" in value:
        import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors

        out["errors"] = (
            aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateDelegationByAssessmentResponse:
    out: BatchCreateDelegationByAssessmentResponse = {}  # type: ignore[typeddict-item]
    if "delegations" in data:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if "errors" in data:
        import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors

        out["errors"] = (
            aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
