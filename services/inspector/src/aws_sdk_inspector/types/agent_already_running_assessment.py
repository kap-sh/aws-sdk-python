"""Generated from Smithy shape ``com.amazonaws.inspector#AgentAlreadyRunningAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_id
    import aws_sdk_inspector.types.arn


class AgentAlreadyRunningAssessment(TypedDict):
    agent_id: "aws_sdk_inspector.types.agent_id.AgentId"
    """<p>ID of the agent that is running on an EC2 instance that is already participating in another started assessment run.</p>"""
    assessment_run_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that has already been started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAlreadyRunningAssessment) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["assessmentRunArn"] = value["assessment_run_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentAlreadyRunningAssessment:
    out: AgentAlreadyRunningAssessment = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentAlreadyRunningAssessment.agent_id required")
    if "assessmentRunArn" in data:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        raise DeserializationError(
            "AgentAlreadyRunningAssessment.assessment_run_arn required"
        )
    return out
