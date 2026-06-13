"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolUseResultData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.json_document
    import aws_sdk_qconnect.types.non_empty_string


class ToolUseResultData(TypedDict):
    tool_use_id: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the tool use instance.</p>"""
    tool_name: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the tool that was used.</p>"""
    tool_result: "aws_sdk_qconnect.types.json_document.JSONDocument"
    """<p>The result of the tool usage.</p>"""
    input_schema: NotRequired["aws_sdk_qconnect.types.json_document.JSONDocument"]
    """<p>The input schema for the tool use result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseResultData) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["toolName"] = value["tool_name"]
    out["toolResult"] = value["tool_result"]
    if "input_schema" in value:
        out["inputSchema"] = value["input_schema"]
    return out


def deserialize_json(data: dict) -> ToolUseResultData:
    out: ToolUseResultData = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("ToolUseResultData.tool_use_id required")
    if "toolName" in data:
        out["tool_name"] = data["toolName"]
    else:
        raise DeserializationError("ToolUseResultData.tool_name required")
    if "toolResult" in data:
        out["tool_result"] = data["toolResult"]
    else:
        raise DeserializationError("ToolUseResultData.tool_result required")
    if "inputSchema" in data:
        out["input_schema"] = data["inputSchema"]
    return out
