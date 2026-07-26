"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_state

AssessmentRunStateList: TypeAlias = list[
    "capo_inspector.types.assessment_run_state.AssessmentRunState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunStateList) -> list:
    import capo_inspector.types.assessment_run_state

    out: list = []
    for item in value:
        out.append(
            capo_inspector.types.assessment_run_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunStateList:
    import capo_inspector.types.assessment_run_state

    out: AssessmentRunStateList = []
    for item in data:
        out.append(
            capo_inspector.types.assessment_run_state.deserialize_aws_json_1_1(item)
        )
    return out
