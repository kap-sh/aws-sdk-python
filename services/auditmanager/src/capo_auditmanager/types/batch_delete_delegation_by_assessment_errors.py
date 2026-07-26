"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_error

BatchDeleteDelegationByAssessmentErrors: TypeAlias = list[
    "capo_auditmanager.types.batch_delete_delegation_by_assessment_error.BatchDeleteDelegationByAssessmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentErrors) -> list:
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_error

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.batch_delete_delegation_by_assessment_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDelegationByAssessmentErrors:
    import capo_auditmanager.types.batch_delete_delegation_by_assessment_error

    out: BatchDeleteDelegationByAssessmentErrors = []
    for item in data:
        out.append(
            capo_auditmanager.types.batch_delete_delegation_by_assessment_error.deserialize_json(
                item
            )
        )
    return out
