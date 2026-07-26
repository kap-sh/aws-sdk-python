"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyAnnotationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_annotation_list
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.timestamp


class GetAutomatedReasoningPolicyAnnotationsResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
    """<p>The name of the Automated Reasoning policy.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList"
    """<p>The current set of annotations containing rules, variables, and types extracted from the source documents. These can be modified before finalizing the policy.</p>"""
    annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash"
    """<p>A hash value representing the current state of the annotations. This is used for optimistic concurrency control when updating annotations.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the annotations were last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyAnnotationsResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["name"] = value["name"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    import capo_bedrock.types.automated_reasoning_policy_annotation_list

    out["annotations"] = (
        capo_bedrock.types.automated_reasoning_policy_annotation_list.serialize_json(
            value["annotations"]
        )
    )
    out["annotationSetHash"] = value["annotation_set_hash"]
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyAnnotationsResponse:
    out: GetAutomatedReasoningPolicyAnnotationsResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.policy_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.name required"
        )
    if "buildWorkflowId" in data:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.build_workflow_id required"
        )
    if "annotations" in data:
        import capo_bedrock.types.automated_reasoning_policy_annotation_list

        out["annotations"] = (
            capo_bedrock.types.automated_reasoning_policy_annotation_list.deserialize_json(
                data["annotations"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.annotations required"
        )
    if "annotationSetHash" in data:
        out["annotation_set_hash"] = data["annotationSetHash"]
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.annotation_set_hash required"
        )
    if "updatedAt" in data:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyAnnotationsResponse.updated_at required"
        )
    return out
