"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningLogicStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement

AutomatedReasoningLogicStatementList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_logic_statement.AutomatedReasoningLogicStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningLogicStatementList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_logic_statement.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningLogicStatementList:
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement

    out: AutomatedReasoningLogicStatementList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_logic_statement.deserialize_json(
                item
            )
        )
    return out
