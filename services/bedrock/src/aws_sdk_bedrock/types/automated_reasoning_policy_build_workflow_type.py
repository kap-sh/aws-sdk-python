"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "INGEST_CONTENT",
        "REFINE_POLICY",
        "IMPORT_POLICY",
        "GENERATE_FIDELITY_REPORT",
        "GENERATE_POLICY_SCENARIOS",
        "RESOLVE_POLICY_AMBIGUITIES",
        "ITERATIVELY_REFINE_POLICY",
    )
)


def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowType) -> str:
    return value


def deserialize_json(data: str) -> AutomatedReasoningPolicyBuildWorkflowType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AutomatedReasoningPolicyBuildWorkflowType value: {data!r}"
        )
    return cast(AutomatedReasoningPolicyBuildWorkflowType, data)
