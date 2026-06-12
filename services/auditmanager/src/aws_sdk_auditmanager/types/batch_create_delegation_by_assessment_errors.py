"""Generated from Smithy shape ``com.amazonaws.auditmanager#BatchCreateDelegationByAssessmentErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error

BatchCreateDelegationByAssessmentErrors: TypeAlias = list[
    "aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error.BatchCreateDelegationByAssessmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateDelegationByAssessmentErrors) -> list:
    import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateDelegationByAssessmentErrors:
    import aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error

    out: BatchCreateDelegationByAssessmentErrors = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.batch_create_delegation_by_assessment_error.deserialize_json(
                item
            )
        )
    return out
