"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.create_assessment_framework_control_set

CreateAssessmentFrameworkControlSets: TypeAlias = list[
    "aws_sdk_auditmanager.types.create_assessment_framework_control_set.CreateAssessmentFrameworkControlSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkControlSets) -> list:
    import aws_sdk_auditmanager.types.create_assessment_framework_control_set

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.create_assessment_framework_control_set.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateAssessmentFrameworkControlSets:
    import aws_sdk_auditmanager.types.create_assessment_framework_control_set

    out: CreateAssessmentFrameworkControlSets = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.create_assessment_framework_control_set.deserialize_json(
                item
            )
        )
    return out
