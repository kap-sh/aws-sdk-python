"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.parameter

ParameterList: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.parameter.Parameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParameterList:
    import aws_sdk_bedrock_agent_runtime.types.parameter

    out: ParameterList = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.parameter.deserialize_json(item))
    return out
