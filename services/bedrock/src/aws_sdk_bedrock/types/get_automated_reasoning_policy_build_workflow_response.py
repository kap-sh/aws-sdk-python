"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyBuildWorkflowResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type
    import aws_sdk_bedrock.types.timestamp


class GetAutomatedReasoningPolicyBuildWorkflowResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    status: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_status.AutomatedReasoningPolicyBuildWorkflowStatus"
    """<p>The current status of the build workflow (e.g., RUNNING, COMPLETED, FAILED, CANCELLED).</p>"""
    build_workflow_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType"
    """<p>The type of build workflow being executed (e.g., DOCUMENT_INGESTION, POLICY_REPAIR).</p>"""
    document_name: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    ]
    """<p>The name of the source document used in the build workflow.</p>"""
    document_content_type: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType"
    ]
    """<p>The content type of the source document (e.g., text/plain, application/pdf).</p>"""
    document_description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_description.AutomatedReasoningPolicyBuildDocumentDescription"
    ]
    """<p>A detailed description of the document's content and how it should be used in the policy generation process.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyBuildWorkflowResponse) -> dict:
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
    if "document_name" in value:
        out["documentName"] = value["document_name"]
    if "document_content_type" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["documentContentType"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.serialize_json(
                value["document_content_type"]
            )
        )
    if "document_description" in value:
        out["documentDescription"] = value["document_description"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyBuildWorkflowResponse:
    out: GetAutomatedReasoningPolicyBuildWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.policy_arn required"
        )
    if "buildWorkflowId" in data:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.build_workflow_id required"
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
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.status required"
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
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.build_workflow_type required"
        )
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    if "documentContentType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["document_content_type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.deserialize_json(
                data["documentContentType"]
            )
        )
    if "documentDescription" in data:
        out["document_description"] = data["documentDescription"]
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.created_at required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyBuildWorkflowResponse.updated_at required"
        )
    return out
