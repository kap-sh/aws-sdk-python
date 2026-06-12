"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_state

AssessmentRunStateList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_run_state.AssessmentRunState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunStateList) -> list:
    import aws_sdk_inspector.types.assessment_run_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_run_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunStateList:
    import aws_sdk_inspector.types.assessment_run_state

    out: AssessmentRunStateList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_run_state.deserialize_aws_json_1_1(item)
        )
    return out
