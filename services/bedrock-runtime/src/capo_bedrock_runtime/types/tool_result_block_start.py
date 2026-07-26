"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultBlockStart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_result_status
    import capo_bedrock_runtime.types.tool_use_id


class ToolResultBlockStart(TypedDict, closed=True):
    tool_use_id: "capo_bedrock_runtime.types.tool_use_id.ToolUseId"
    """<p>The ID of the tool that was used to generate this tool result block.</p>"""
    type: NotRequired["str"]
    """<p>The type for the tool that was used to generate this tool result block.</p>"""
    status: NotRequired[
        "capo_bedrock_runtime.types.tool_result_status.ToolResultStatus"
    ]
    """<p>The status of the tool result block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultBlockStart) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    if "type" in value:
        out["type"] = value["type"]
    if "status" in value:
        import capo_bedrock_runtime.types.tool_result_status

        out["status"] = capo_bedrock_runtime.types.tool_result_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> ToolResultBlockStart:
    out: ToolResultBlockStart = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("ToolResultBlockStart.tool_use_id required")
    if "type" in data:
        out["type"] = data["type"]
    if "status" in data:
        import capo_bedrock_runtime.types.tool_result_status

        out["status"] = capo_bedrock_runtime.types.tool_result_status.deserialize_json(
            data["status"]
        )
    return out
