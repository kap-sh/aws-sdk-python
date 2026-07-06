"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlock``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_block
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_block
    import aws_sdk_bedrock_agentcore.types.sensitive_text


class _HarnessContentBlock_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessContentBlock_toolUse(TypedDict, closed=True):
    toolUse: (
        "aws_sdk_bedrock_agentcore.types.harness_tool_use_block.HarnessToolUseBlock"
    )


class _HarnessContentBlock_toolResult(TypedDict, closed=True):
    toolResult: "aws_sdk_bedrock_agentcore.types.harness_tool_result_block.HarnessToolResultBlock"


class _HarnessContentBlock_reasoningContent(TypedDict, closed=True):
    reasoningContent: "aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block.HarnessReasoningContentBlock"


HarnessContentBlock: TypeAlias = (
    _HarnessContentBlock_text
    | _HarnessContentBlock_toolUse
    | _HarnessContentBlock_toolResult
    | _HarnessContentBlock_reasoningContent
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_block

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_block.serialize_json(
                value["toolResult"]
            )
        }
    elif "reasoningContent" in value:
        import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block

        return {
            "reasoningContent": aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block.serialize_json(
                value["reasoningContent"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "toolUse" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_block

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_block.deserialize_json(
                data["toolResult"]
            )
        }
    elif "reasoningContent" in data:
        import aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block

        return {
            "reasoningContent": aws_sdk_bedrock_agentcore.types.harness_reasoning_content_block.deserialize_json(
                data["reasoningContent"]
            )
        }
    else:
        raise DeserializationError("HarnessContentBlock: no recognized variant key")
