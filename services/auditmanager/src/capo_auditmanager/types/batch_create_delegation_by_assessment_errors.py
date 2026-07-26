"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.batch_create_delegation_by_assessment_error

BatchCreateDelegationByAssessmentErrors: TypeAlias = list[
    "capo_auditmanager.types.batch_create_delegation_by_assessment_error.BatchCreateDelegationByAssessmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentErrors) -> list:
    import capo_auditmanager.types.batch_create_delegation_by_assessment_error

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.batch_create_delegation_by_assessment_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateDelegationByAssessmentErrors:
    import capo_auditmanager.types.batch_create_delegation_by_assessment_error

    out: BatchCreateDelegationByAssessmentErrors = []
    for item in data:
        out.append(
            capo_auditmanager.types.batch_create_delegation_by_assessment_error.deserialize_json(
                item
            )
        )
    return out
