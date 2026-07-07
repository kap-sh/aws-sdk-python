"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseBlockStart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_name
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_id
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_type


class HarnessToolUseBlockStart(TypedDict, closed=True):
    tool_use_id: "aws_sdk_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The unique ID of this tool use.</p>"""
    name: "aws_sdk_bedrock_agentcore.types.harness_tool_name.HarnessToolName"
    """<p>The name of the tool being called.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_tool_use_type.HarnessToolUseType"
    ]
    """<p>The type of tool use.</p>"""
    server_name: NotRequired["str"]
    """<p>The name of the MCP server providing this tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseBlockStart) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_type.serialize_json(
                value["type"]
            )
        )
    if "server_name" in value:
        out["serverName"] = value["server_name"]
    return out


def deserialize_json(data: dict) -> HarnessToolUseBlockStart:
    out: HarnessToolUseBlockStart = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("HarnessToolUseBlockStart.tool_use_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HarnessToolUseBlockStart.name required")
    if "type" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_type.deserialize_json(
                data["type"]
            )
        )
    if "serverName" in data:
        out["server_name"] = data["serverName"]
    return out
