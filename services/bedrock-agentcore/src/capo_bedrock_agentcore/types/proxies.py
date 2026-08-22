"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Proxies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.proxy

Proxies: TypeAlias = list["capo_bedrock_agentcore.types.proxy.Proxy"]


# --- restJson1 ser/de ---
def serialize_json(value: Proxies) -> list:
    import capo_bedrock_agentcore.types.proxy

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.proxy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Proxies:
    import capo_bedrock_agentcore.types.proxy

    out: Proxies = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.proxy.deserialize_json(item))
    return out
