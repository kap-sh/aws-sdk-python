"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.create_assessment_framework_control_set

CreateAssessmentFrameworkControlSets: TypeAlias = list[
    "capo_auditmanager.types.create_assessment_framework_control_set.CreateAssessmentFrameworkControlSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkControlSets) -> list:
    import capo_auditmanager.types.create_assessment_framework_control_set

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.create_assessment_framework_control_set.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateAssessmentFrameworkControlSets:
    import capo_auditmanager.types.create_assessment_framework_control_set

    out: CreateAssessmentFrameworkControlSets = []
    for item in data:
        out.append(
            capo_auditmanager.types.create_assessment_framework_control_set.deserialize_json(
                item
            )
        )
    return out
