"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class _HarnessContentBlockDelta_text(TypedDict):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessContentBlockDelta_toolUse(TypedDict):
    toolUse: "aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta.HarnessToolUseBlockDelta"


class _HarnessContentBlockDelta_toolResult(TypedDict):
    toolResult: "aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta.HarnessToolResultBlocksDelta"


class _HarnessContentBlockDelta_reasoningContent(TypedDict):
    reasoningContent: "aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta.HarnessReasoningContentBlockDelta"


HarnessContentBlockDelta: TypeAlias = (
    _HarnessContentBlockDelta_text
    | _HarnessContentBlockDelta_toolUse
    | _HarnessContentBlockDelta_toolResult
    | _HarnessContentBlockDelta_reasoningContent
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockDelta) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta.serialize_json(
                value["reasoningContent"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlockDelta:
    if "text" in data:
        return {"text": data["text"]}
    elif "toolUse" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block_delta.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_blocks_delta.deserialize_json(
                data["toolResult"]
            )
        }
    elif "reasoningContent" in data:
        import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block_delta.deserialize_json(
                data["reasoningContent"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessContentBlockDelta: no recognized variant key"
        )
