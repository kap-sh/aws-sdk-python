"""Generated from Smithy shape ``com.amazonaws.inspector#AgentAlreadyRunningAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_already_running_assessment

AgentAlreadyRunningAssessmentList: TypeAlias = list[
    "aws_sdk_inspector.types.agent_already_running_assessment.AgentAlreadyRunningAssessment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAlreadyRunningAssessmentList) -> list:
    import aws_sdk_inspector.types.agent_already_running_assessment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.agent_already_running_assessment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentAlreadyRunningAssessmentList:
    import aws_sdk_inspector.types.agent_already_running_assessment

    out: AgentAlreadyRunningAssessmentList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.agent_already_running_assessment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
