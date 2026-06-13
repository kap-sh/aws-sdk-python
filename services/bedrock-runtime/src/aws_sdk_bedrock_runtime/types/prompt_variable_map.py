"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#PromptVariableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.prompt_variable_values

PromptVariableMap: TypeAlias = dict[
    "str", "aws_sdk_bedrock_runtime.types.prompt_variable_values.PromptVariableValues"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PromptVariableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_runtime.types.prompt_variable_values

        out[key] = aws_sdk_bedrock_runtime.types.prompt_variable_values.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PromptVariableMap:
    out: PromptVariableMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_runtime.types.prompt_variable_values

        out[key] = (
            aws_sdk_bedrock_runtime.types.prompt_variable_values.deserialize_json(value)
        )
    return out
