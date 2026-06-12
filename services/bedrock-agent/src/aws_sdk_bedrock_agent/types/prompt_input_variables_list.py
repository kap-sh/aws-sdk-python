"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptInputVariablesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_input_variable

PromptInputVariablesList: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.prompt_input_variable.PromptInputVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptInputVariablesList) -> list:
    import aws_sdk_bedrock_agent.types.prompt_input_variable

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.prompt_input_variable.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PromptInputVariablesList:
    import aws_sdk_bedrock_agent.types.prompt_input_variable

    out: PromptInputVariablesList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.prompt_input_variable.deserialize_json(item)
        )
    return out
