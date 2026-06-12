"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyStatementReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference

AutomatedReasoningPolicyStatementReferenceList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference.AutomatedReasoningPolicyStatementReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyStatementReferenceList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyStatementReferenceList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference

    out: AutomatedReasoningPolicyStatementReferenceList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_statement_reference.deserialize_json(
                item
            )
        )
    return out
