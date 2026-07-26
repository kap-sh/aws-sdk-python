"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_name
    import capo_bedrock_agentcore.types.harness_tool_use_id
    import capo_bedrock_agentcore.types.harness_tool_use_type
    import capo_bedrock_agentcore.types.sensitive_json


class HarnessToolUseBlock(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.harness_tool_name.HarnessToolName"
    """<p>The name of the tool to call.</p>"""
    tool_use_id: "capo_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The unique ID of this tool use.</p>"""
    input: "capo_bedrock_agentcore.types.sensitive_json.SensitiveJson"
    """<p>The JSON input to pass to the tool.</p>"""
    type: NotRequired[
        "capo_bedrock_agentcore.types.harness_tool_use_type.HarnessToolUseType"
    ]
    """<p>The type of tool use.</p>"""
    server_name: NotRequired["str"]
    """<p>The name of the MCP server providing this tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseBlock) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["toolUseId"] = value["tool_use_id"]
    out["input"] = value["input"]
    if "type" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = capo_bedrock_agentcore.types.harness_tool_use_type.serialize_json(
            value["type"]
        )
    if "server_name" in value:
        out["serverName"] = value["server_name"]
    return out


def deserialize_json(data: dict) -> HarnessToolUseBlock:
    out: HarnessToolUseBlock = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HarnessToolUseBlock.name required")
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("HarnessToolUseBlock.tool_use_id required")
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError("HarnessToolUseBlock.input required")
    if "type" in data:
        import capo_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            capo_bedrock_agentcore.types.harness_tool_use_type.deserialize_json(
                data["type"]
            )
        )
    if "serverName" in data:
        out["server_name"] = data["serverName"]
    return out
