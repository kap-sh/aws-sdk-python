"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.update_assessment_framework_control_set

UpdateAssessmentFrameworkControlSets: TypeAlias = list[
    "aws_sdk_auditmanager.types.update_assessment_framework_control_set.UpdateAssessmentFrameworkControlSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkControlSets) -> list:
    import aws_sdk_auditmanager.types.update_assessment_framework_control_set

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.update_assessment_framework_control_set.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateAssessmentFrameworkControlSets:
    import aws_sdk_auditmanager.types.update_assessment_framework_control_set

    out: UpdateAssessmentFrameworkControlSets = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.update_assessment_framework_control_set.deserialize_json(
                item
            )
        )
    return out
