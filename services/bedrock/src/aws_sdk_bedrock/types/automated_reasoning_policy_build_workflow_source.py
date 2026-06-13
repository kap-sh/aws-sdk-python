"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_definition
    import aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content


class AutomatedReasoningPolicyBuildWorkflowSource(TypedDict):
    policy_definition: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
    ]
    """<p>An existing policy definition that serves as the starting point for the build workflow, typically used in policy repair or update scenarios.</p>"""
    workflow_content: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content.AutomatedReasoningPolicyWorkflowTypeContent"
    ]
    """<p>The actual content to be processed in the build workflow, such as documents to analyze or repair instructions to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowSource) -> dict:
    out: dict = {}
    if "policy_definition" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        out["policyDefinition"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition.serialize_json(
                value["policy_definition"]
            )
        )
    if "workflow_content" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content

        out["workflowContent"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content.serialize_json(
                value["workflow_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowSource:
    out: AutomatedReasoningPolicyBuildWorkflowSource = {}  # type: ignore[typeddict-item]
    if "policyDefinition" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_definition

        out["policy_definition"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_definition.deserialize_json(
                data["policyDefinition"]
            )
        )
    if "workflowContent" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content

        out["workflow_content"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_workflow_type_content.deserialize_json(
                data["workflowContent"]
            )
        )
    return out
