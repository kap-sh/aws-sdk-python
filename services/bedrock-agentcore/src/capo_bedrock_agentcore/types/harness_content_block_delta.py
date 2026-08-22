"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockDelta``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta
    import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta
    import capo_bedrock_agentcore.types.harness_tool_use_block_delta
    import capo_bedrock_agentcore.types.sensitive_text


class _HarnessContentBlockDelta_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessContentBlockDelta_toolUse(TypedDict, closed=True):
    toolUse: "capo_bedrock_agentcore.types.harness_tool_use_block_delta.HarnessToolUseBlockDelta"


class _HarnessContentBlockDelta_toolResult(TypedDict, closed=True):
    toolResult: "capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.HarnessToolResultBlocksDelta"


class _HarnessContentBlockDelta_reasoningContent(TypedDict, closed=True):
    reasoningContent: "capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.HarnessReasoningContentBlockDelta"


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
        import capo_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_delta.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.serialize_json(
                value["reasoningContent"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlockDelta: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("toolUse") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_block_delta

        return {
            "toolUse": capo_bedrock_agentcore.types.harness_tool_use_block_delta.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_blocks_delta

        return {
            "toolResult": capo_bedrock_agentcore.types.harness_tool_result_blocks_delta.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("reasoningContent") is not None:
        import capo_bedrock_agentcore.types.harness_reasoning_content_block_delta

        return {
            "reasoningContent": capo_bedrock_agentcore.types.harness_reasoning_content_block_delta.deserialize_json(
                data["reasoningContent"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessContentBlockDelta: no recognized variant key"
        )
