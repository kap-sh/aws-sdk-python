"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_summary

CodeInterpreterSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.code_interpreter_summary.CodeInterpreterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSummaries) -> list:
    import capo_bedrock_agentcore_control.types.code_interpreter_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.code_interpreter_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeInterpreterSummaries:
    import capo_bedrock_agentcore_control.types.code_interpreter_summary

    out: CodeInterpreterSummaries = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.code_interpreter_summary.deserialize_json(
                item
            )
        )
    return out
