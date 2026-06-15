"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlock``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_id
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_status
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_type


class HarnessToolResultBlock(TypedDict):
    tool_use_id: "aws_sdk_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The tool use ID that this result corresponds to.</p>"""
    content: "aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks.HarnessToolResultContentBlocks"
    """<p>The content of the tool result.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_tool_use_status.HarnessToolUseStatus"
    ]
    """<p>The status of the tool execution.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_tool_use_type.HarnessToolUseType"
    ]
    """<p>The type of tool use that produced this result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlock) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks

    out["content"] = (
        aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks.serialize_json(
            value["content"]
        )
    )
    if "status" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_status.serialize_json(
                value["status"]
            )
        )
    if "type" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessToolResultBlock:
    out: HarnessToolResultBlock = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("HarnessToolResultBlock.tool_use_id required")
    if "content" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks

        out["content"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_result_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("HarnessToolResultBlock.content required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_status.deserialize_json(
                data["status"]
            )
        )
    if "type" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_type.deserialize_json(
                data["type"]
            )
        )
    return out
