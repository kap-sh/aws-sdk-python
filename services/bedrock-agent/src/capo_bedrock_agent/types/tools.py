"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Tools``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.tool

Tools: TypeAlias = list["capo_bedrock_agent.types.tool.Tool"]


# --- restJson1 ser/de ---
def serialize_json(value: Tools) -> list:
    import capo_bedrock_agent.types.tool

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.tool.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tools:
    import capo_bedrock_agent.types.tool

    out: Tools = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.tool.deserialize_json(item))
    return out
