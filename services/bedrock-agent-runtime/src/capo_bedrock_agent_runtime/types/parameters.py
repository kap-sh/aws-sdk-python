"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.parameter

Parameters: TypeAlias = list["capo_bedrock_agent_runtime.types.parameter.Parameter"]


# --- restJson1 ser/de ---
def serialize_json(value: Parameters) -> list:
    import capo_bedrock_agent_runtime.types.parameter

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> Parameters:
    import capo_bedrock_agent_runtime.types.parameter

    out: Parameters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.parameter.deserialize_json(item))
    return out
