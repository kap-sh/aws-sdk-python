"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FunctionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.function_parameter

FunctionParameters: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.function_parameter.FunctionParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionParameters) -> list:
    import capo_bedrock_agent_runtime.types.function_parameter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.function_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FunctionParameters:
    import capo_bedrock_agent_runtime.types.function_parameter

    out: FunctionParameters = []
    for item in data:
        out.append(
            capo_bedrock_agent_runtime.types.function_parameter.deserialize_json(item)
        )
    return out
