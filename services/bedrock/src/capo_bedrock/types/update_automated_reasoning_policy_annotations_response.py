"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyAnnotationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.timestamp


class UpdateAutomatedReasoningPolicyAnnotationsResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>The new hash value representing the updated state of the annotations.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the annotations were updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyAnnotationsResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    out["annotationSetHash"] = value["annotation_set_hash"]
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyAnnotationsResponse:
    out: UpdateAutomatedReasoningPolicyAnnotationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyAnnotationsResponse.policy_arn required"
        )
    if data.get("buildWorkflowId") is not None:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyAnnotationsResponse.build_workflow_id required"
        )
    if data.get("annotationSetHash") is not None:
        out["annotation_set_hash"] = data["annotationSetHash"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyAnnotationsResponse.annotation_set_hash required"
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyAnnotationsResponse.updated_at required"
        )
    return out
