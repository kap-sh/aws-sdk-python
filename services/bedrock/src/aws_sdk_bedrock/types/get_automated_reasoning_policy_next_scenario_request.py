"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyNextScenarioRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id


class GetAutomatedReasoningPolicyNextScenarioRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which you want to get the next test scenario.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow associated with the test scenarios.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyNextScenarioRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyNextScenarioRequest:
    out: GetAutomatedReasoningPolicyNextScenarioRequest = {}  # type: ignore[typeddict-item]
    return out
