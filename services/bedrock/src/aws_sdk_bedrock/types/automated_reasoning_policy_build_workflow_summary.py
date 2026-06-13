"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type
    import aws_sdk_bedrock.types.timestamp


class AutomatedReasoningPolicyBuildWorkflowSummary(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy associated with this build workflow.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    status: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status.AutomatedReasoningPolicyBuildWorkflowStatus"
    """<p>The current status of the build workflow (e.g., RUNNING, COMPLETED, FAILED, CANCELLED).</p>"""
    build_workflow_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType"
    """<p>The type of build workflow (e.g., DOCUMENT_INGESTION, POLICY_REPAIR).</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowSummary) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status

    out["status"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type

    out["buildWorkflowType"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type.serialize_json(
            value["build_workflow_type"]
        )
    )
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowSummary:
    out: AutomatedReasoningPolicyBuildWorkflowSummary = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.policy_arn required"
        )
    if "buildWorkflowId" in data:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.build_workflow_id required"
        )
    if "status" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status

        out["status"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.status required"
        )
    if "buildWorkflowType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type

        out["build_workflow_type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type.deserialize_json(
                data["buildWorkflowType"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.build_workflow_type required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowSummary.updated_at required"
        )
    return out
