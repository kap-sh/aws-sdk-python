"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyWorkflowTypeContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content
    import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content
    import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content


class _AutomatedReasoningPolicyWorkflowTypeContent_documents(TypedDict, closed=True):
    documents: "capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list.AutomatedReasoningPolicyBuildWorkflowDocumentList"


class _AutomatedReasoningPolicyWorkflowTypeContent_policyRepairAssets(
    TypedDict, closed=True
):
    policyRepairAssets: "capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content.AutomatedReasoningPolicyBuildWorkflowRepairContent"


class _AutomatedReasoningPolicyWorkflowTypeContent_generateFidelityReportContent(
    TypedDict, closed=True
):
    generateFidelityReportContent: "capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content.AutomatedReasoningPolicyGenerateFidelityReportContent"


class _AutomatedReasoningPolicyWorkflowTypeContent_iterativeRefinementContent(
    TypedDict, closed=True
):
    iterativeRefinementContent: "capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content.AutomatedReasoningPolicyIterativeRefinementContent"


AutomatedReasoningPolicyWorkflowTypeContent: TypeAlias = (
    _AutomatedReasoningPolicyWorkflowTypeContent_documents
    | _AutomatedReasoningPolicyWorkflowTypeContent_policyRepairAssets
    | _AutomatedReasoningPolicyWorkflowTypeContent_generateFidelityReportContent
    | _AutomatedReasoningPolicyWorkflowTypeContent_iterativeRefinementContent
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyWorkflowTypeContent) -> dict:
    if "documents" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list

        return {
            "documents": capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list.serialize_json(
                value["documents"]
            )
        }
    elif "policyRepairAssets" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content

        return {
            "policyRepairAssets": capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content.serialize_json(
                value["policyRepairAssets"]
            )
        }
    elif "generateFidelityReportContent" in value:
        import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content

        return {
            "generateFidelityReportContent": capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content.serialize_json(
                value["generateFidelityReportContent"]
            )
        }
    elif "iterativeRefinementContent" in value:
        import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content

        return {
            "iterativeRefinementContent": capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content.serialize_json(
                value["iterativeRefinementContent"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyWorkflowTypeContent: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyWorkflowTypeContent:
    if "documents" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list

        return {
            "documents": capo_bedrock.types.automated_reasoning_policy_build_workflow_document_list.deserialize_json(
                data["documents"]
            )
        }
    elif "policyRepairAssets" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content

        return {
            "policyRepairAssets": capo_bedrock.types.automated_reasoning_policy_build_workflow_repair_content.deserialize_json(
                data["policyRepairAssets"]
            )
        }
    elif "generateFidelityReportContent" in data:
        import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content

        return {
            "generateFidelityReportContent": capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_content.deserialize_json(
                data["generateFidelityReportContent"]
            )
        }
    elif "iterativeRefinementContent" in data:
        import capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content

        return {
            "iterativeRefinementContent": capo_bedrock.types.automated_reasoning_policy_iterative_refinement_content.deserialize_json(
                data["iterativeRefinementContent"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyWorkflowTypeContent: no recognized variant key"
        )
