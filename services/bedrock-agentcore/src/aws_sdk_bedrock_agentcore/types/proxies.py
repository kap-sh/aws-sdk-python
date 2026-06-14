"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Proxies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.proxy

Proxies: TypeAlias = list["aws_sdk_bedrock_agentcore.types.proxy.Proxy"]


# --- restJson1 ser/de ---
def serialize_json(value: Proxies) -> list:
    import aws_sdk_bedrock_agentcore.types.proxy

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.proxy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Proxies:
    import aws_sdk_bedrock_agentcore.types.proxy

    out: Proxies = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.proxy.deserialize_json(item))
    return out
