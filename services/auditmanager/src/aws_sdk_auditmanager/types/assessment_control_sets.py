"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControlSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_control_set

AssessmentControlSets: TypeAlias = list[
    "aws_sdk_auditmanager.types.assessment_control_set.AssessmentControlSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControlSets) -> list:
    import aws_sdk_auditmanager.types.assessment_control_set

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.assessment_control_set.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentControlSets:
    import aws_sdk_auditmanager.types.assessment_control_set

    out: AssessmentControlSets = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.assessment_control_set.deserialize_json(item)
        )
    return out
