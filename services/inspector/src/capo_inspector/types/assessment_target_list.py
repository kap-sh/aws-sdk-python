"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.assessment_target

AssessmentTargetList: TypeAlias = list[
    "capo_inspector.types.assessment_target.AssessmentTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentTargetList) -> list:
    import capo_inspector.types.assessment_target

    out: list = []
    for item in value:
        out.append(capo_inspector.types.assessment_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentTargetList:
    import capo_inspector.types.assessment_target

    out: AssessmentTargetList = []
    for item in data:
        out.append(
            capo_inspector.types.assessment_target.deserialize_aws_json_1_1(item)
        )
    return out
