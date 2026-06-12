"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchDeleteDelegationByAssessmentErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error

BatchDeleteDelegationByAssessmentErrors: TypeAlias = list[
    "aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error.BatchDeleteDelegationByAssessmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDelegationByAssessmentErrors) -> list:
    import aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDelegationByAssessmentErrors:
    import aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error

    out: BatchDeleteDelegationByAssessmentErrors = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.batch_delete_delegation_by_assessment_error.deserialize_json(
                item
            )
        )
    return out
