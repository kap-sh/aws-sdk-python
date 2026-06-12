"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunAgentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_agent

AssessmentRunAgentList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_run_agent.AssessmentRunAgent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunAgentList) -> list:
    import aws_sdk_inspector.types.assessment_run_agent

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_run_agent.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunAgentList:
    import aws_sdk_inspector.types.assessment_run_agent

    out: AssessmentRunAgentList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_run_agent.deserialize_aws_json_1_1(item)
        )
    return out
