"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowType``."""

from typing import Literal, TypeAlias, cast

AutomatedReasoningPolicyBuildWorkflowType: TypeAlias = Literal[
    "INGEST_CONTENT",
    "REFINE_POLICY",
    "IMPORT_POLICY",
    "GENERATE_FIDELITY_REPORT",
    "GENERATE_POLICY_SCENARIOS",
    "RESOLVE_POLICY_AMBIGUITIES",
    "ITERATIVELY_REFINE_POLICY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowType:
    return cast(AutomatedReasoningPolicyBuildWorkflowType, data)
