"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Functions``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.function_definition

Functions: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.function_definition.FunctionDefinition"]


# --- restJson1 ser/de ---
def serialize_json(value: Functions) -> list:
    import aws_sdk_bedrock_agent_runtime.types.function_definition
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.function_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Functions:
    import aws_sdk_bedrock_agent_runtime.types.function_definition
    out: Functions = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.function_definition.deserialize_json(item))
    return out