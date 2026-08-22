"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Functions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.function

Functions: TypeAlias = list["capo_bedrock_agent.types.function.Function"]


# --- restJson1 ser/de ---
def serialize_json(value: Functions) -> list:
    import capo_bedrock_agent.types.function

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.function.serialize_json(item))
    return out


def deserialize_json(data: list) -> Functions:
    import capo_bedrock_agent.types.function

    out: Functions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.function.deserialize_json(item))
    return out
