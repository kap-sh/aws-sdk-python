"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CodeInterpreterSessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.code_interpreter_session_summary

CodeInterpreterSessionSummaries: TypeAlias = list[
    "capo_bedrock_agentcore.types.code_interpreter_session_summary.CodeInterpreterSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSessionSummaries) -> list:
    import capo_bedrock_agentcore.types.code_interpreter_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.code_interpreter_session_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeInterpreterSessionSummaries:
    import capo_bedrock_agentcore.types.code_interpreter_session_summary

    out: CodeInterpreterSessionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore.types.code_interpreter_session_summary.deserialize_json(
                item
            )
        )
    return out
