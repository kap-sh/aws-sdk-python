"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.parameter

ParameterList: TypeAlias = list["capo_bedrock_agent_runtime.types.parameter.Parameter"]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterList) -> list:
    import capo_bedrock_agent_runtime.types.parameter

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParameterList:
    import capo_bedrock_agent_runtime.types.parameter

    out: ParameterList = []
    for item in data:
        out.append(capo_bedrock_agent_runtime.types.parameter.deserialize_json(item))
    return out
