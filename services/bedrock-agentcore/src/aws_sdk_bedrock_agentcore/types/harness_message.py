"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_content_blocks
    import aws_sdk_bedrock_agentcore.types.harness_conversation_role


class HarnessMessage(TypedDict):
    role: "aws_sdk_bedrock_agentcore.types.harness_conversation_role.HarnessConversationRole"
    """<p>The role of the message sender.</p>"""
    content: (
        "aws_sdk_bedrock_agentcore.types.harness_content_blocks.HarnessContentBlocks"
    )
    """<p>The content blocks of the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessage) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.harness_conversation_role

    out["role"] = (
        aws_sdk_bedrock_agentcore.types.harness_conversation_role.serialize_json(
            value["role"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.harness_content_blocks

    out["content"] = (
        aws_sdk_bedrock_agentcore.types.harness_content_blocks.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> HarnessMessage:
    out: HarnessMessage = {}  # type: ignore[typeddict-item]
    if "role" in data:
        import aws_sdk_bedrock_agentcore.types.harness_conversation_role

        out["role"] = (
            aws_sdk_bedrock_agentcore.types.harness_conversation_role.deserialize_json(
                data["role"]
            )
        )
    else:
        raise DeserializationError("HarnessMessage.role required")
    if "content" in data:
        import aws_sdk_bedrock_agentcore.types.harness_content_blocks

        out["content"] = (
            aws_sdk_bedrock_agentcore.types.harness_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("HarnessMessage.content required")
    return out
