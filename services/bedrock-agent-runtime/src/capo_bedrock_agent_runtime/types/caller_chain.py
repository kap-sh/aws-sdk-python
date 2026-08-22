"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CallerChain``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.caller

CallerChain: TypeAlias = list["capo_bedrock_agent_runtime.types.caller.Caller"]


# --- restJson1 ser/de ---
def serialize_json(value: CallerChain) -> list:
    import capo_bedrock_agent_runtime.types.caller

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.caller.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallerChain:
    import capo_bedrock_agent_runtime.types.caller

    out: CallerChain = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.caller.deserialize_json(item))
    return out
