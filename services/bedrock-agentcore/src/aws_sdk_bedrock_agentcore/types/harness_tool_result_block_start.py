"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlockStart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_id
    import aws_sdk_bedrock_agentcore.types.harness_tool_use_status


class HarnessToolResultBlockStart(TypedDict):
    tool_use_id: "aws_sdk_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The tool use ID that this result corresponds to.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_tool_use_status.HarnessToolUseStatus"
    ]
    """<p>The status of the tool execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlockStart) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    if "status" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessToolResultBlockStart:
    out: HarnessToolResultBlockStart = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("HarnessToolResultBlockStart.tool_use_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.harness_tool_use_status.deserialize_json(
                data["status"]
            )
        )
    return out
