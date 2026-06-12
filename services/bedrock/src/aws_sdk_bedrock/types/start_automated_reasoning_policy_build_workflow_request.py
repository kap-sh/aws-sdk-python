"""Generated from Smithy shape ``com.amazonaws.bedrock#StartAutomatedReasoningPolicyBuildWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type
    import aws_sdk_bedrock.types.idempotency_token


class StartAutomatedReasoningPolicyBuildWorkflowRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.</p>"""
    build_workflow_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType"
    """<p>The type of build workflow to start (e.g., DOCUMENT_INGESTION for processing new documents, POLICY_REPAIR for fixing existing policies).</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>"""
    source_content: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source.AutomatedReasoningPolicyBuildWorkflowSource"
    """<p>The source content for the build workflow, such as documents to analyze or repair instructions for existing policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomatedReasoningPolicyBuildWorkflowRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source

    out["sourceContent"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source.serialize_json(
            value["source_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartAutomatedReasoningPolicyBuildWorkflowRequest:
    out: StartAutomatedReasoningPolicyBuildWorkflowRequest = {}  # type: ignore[typeddict-item]
    if "sourceContent" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source

        out["source_content"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_source.deserialize_json(
                data["sourceContent"]
            )
        )
    else:
        raise DeserializationError(
            "StartAutomatedReasoningPolicyBuildWorkflowRequest.source_content required"
        )
    return out
