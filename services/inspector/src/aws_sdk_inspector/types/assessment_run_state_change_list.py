"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunStateChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_state_change

AssessmentRunStateChangeList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_run_state_change.AssessmentRunStateChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunStateChangeList) -> list:
    import aws_sdk_inspector.types.assessment_run_state_change

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_run_state_change.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunStateChangeList:
    import aws_sdk_inspector.types.assessment_run_state_change

    out: AssessmentRunStateChangeList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_run_state_change.deserialize_aws_json_1_1(
                item
            )
        )
    return out
