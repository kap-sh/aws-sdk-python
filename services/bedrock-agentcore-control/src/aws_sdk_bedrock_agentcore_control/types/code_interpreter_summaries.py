"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary

CodeInterpreterSummaries: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary.CodeInterpreterSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeInterpreterSummaries:
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary
    out: CodeInterpreterSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.code_interpreter_summary.deserialize_json(item))
    return out