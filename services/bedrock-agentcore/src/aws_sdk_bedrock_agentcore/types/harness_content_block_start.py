"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessContentBlockStart``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start


class _HarnessContentBlockStart_toolUse(TypedDict):
    toolUse: "aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start.HarnessToolUseBlockStart"


class _HarnessContentBlockStart_toolResult(TypedDict):
    toolResult: "aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start.HarnessToolResultBlockStart"


HarnessContentBlockStart: TypeAlias = (
    _HarnessContentBlockStart_toolUse | _HarnessContentBlockStart_toolResult
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessContentBlockStart) -> dict:
    if "toolUse" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start.serialize_json(
                value["toolResult"]
            )
        }
    else:
        raise SerializationError("HarnessContentBlockStart: no variant present")


def deserialize_json(data: dict) -> HarnessContentBlockStart:
    if "toolUse" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start

        return {
            "toolUse": aws_sdk_bedrock_agentcore.types.harness_tool_use_block_start.deserialize_json(
                data["toolUse"]
            )
        }
    elif "toolResult" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start

        return {
            "toolResult": aws_sdk_bedrock_agentcore.types.harness_tool_result_block_start.deserialize_json(
                data["toolResult"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessContentBlockStart: no recognized variant key"
        )
