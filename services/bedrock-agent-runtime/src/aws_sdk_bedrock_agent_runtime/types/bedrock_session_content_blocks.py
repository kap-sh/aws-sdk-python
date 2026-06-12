"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockSessionContentBlocks``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block

BedrockSessionContentBlocks: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block.BedrockSessionContentBlock"]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockSessionContentBlocks) -> list:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> BedrockSessionContentBlocks:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block
    out: BedrockSessionContentBlocks = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.bedrock_session_content_block.deserialize_json(item))
    return out