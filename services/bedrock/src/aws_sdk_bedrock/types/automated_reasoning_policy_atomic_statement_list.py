"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAtomicStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement

AutomatedReasoningPolicyAtomicStatementList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement.AutomatedReasoningPolicyAtomicStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAtomicStatementList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyAtomicStatementList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement

    out: AutomatedReasoningPolicyAtomicStatementList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement.deserialize_json(
                item
            )
        )
    return out
