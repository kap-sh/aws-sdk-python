"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyIterativeRefinementContent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_feedback
    import aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list


class AutomatedReasoningPolicyIterativeRefinementContent(TypedDict):
    documents: "aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.AutomatedReasoningPolicyIterativeRefinementDocumentList"
    """<p>Source documents used for iterative policy refinement. These documents provide context for refining the policy definition.</p>"""
    feedback: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_feedback.AutomatedReasoningPolicyBuildFeedback"
    ]
    """<p>Optional feedback to guide the iterative refinement workflow. Provide specific instructions or constraints for policy refinement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyIterativeRefinementContent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list

    out["documents"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.serialize_json(
            value["documents"]
        )
    )
    if "feedback" in value:
        out["feedback"] = value["feedback"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyIterativeRefinementContent:
    out: AutomatedReasoningPolicyIterativeRefinementContent = {}  # type: ignore[typeddict-item]
    if "documents" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list

        out["documents"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_iterative_refinement_document_list.deserialize_json(
                data["documents"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyIterativeRefinementContent.documents required"
        )
    if "feedback" in data:
        out["feedback"] = data["feedback"]
    return out
