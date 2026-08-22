"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyStatementReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_statement_reference

AutomatedReasoningPolicyStatementReferenceList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_statement_reference.AutomatedReasoningPolicyStatementReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyStatementReferenceList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_statement_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_statement_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyStatementReferenceList:
    import capo_bedrock.types.automated_reasoning_policy_statement_reference

    out: AutomatedReasoningPolicyStatementReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_statement_reference.deserialize_json(
                item
            )
        )
    return out
