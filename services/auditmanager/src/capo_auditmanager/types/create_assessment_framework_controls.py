"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.create_assessment_framework_control

CreateAssessmentFrameworkControls: TypeAlias = list[
    "capo_auditmanager.types.create_assessment_framework_control.CreateAssessmentFrameworkControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkControls) -> list:
    import capo_auditmanager.types.create_assessment_framework_control

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.create_assessment_framework_control.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateAssessmentFrameworkControls:
    import capo_auditmanager.types.create_assessment_framework_control

    out: CreateAssessmentFrameworkControls = []
    for item in data:
        out.append(
            capo_auditmanager.types.create_assessment_framework_control.deserialize_json(
                item
            )
        )
    return out
