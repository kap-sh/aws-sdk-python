"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CallerChain``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.caller

CallerChain: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.caller.Caller"]


# --- restJson1 ser/de ---
def serialize_json(value: CallerChain) -> list:
    import aws_sdk_bedrock_agent_runtime.types.caller
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.caller.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallerChain:
    import aws_sdk_bedrock_agent_runtime.types.caller
    out: CallerChain = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.caller.deserialize_json(item))
    return out