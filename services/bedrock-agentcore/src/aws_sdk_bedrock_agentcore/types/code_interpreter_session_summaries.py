"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterSessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary

CodeInterpreterSessionSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary.CodeInterpreterSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSessionSummaries) -> list:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeInterpreterSessionSummaries:
    import aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary

    out: CodeInterpreterSessionSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.code_interpreter_session_summary.deserialize_json(
                item
            )
        )
    return out
