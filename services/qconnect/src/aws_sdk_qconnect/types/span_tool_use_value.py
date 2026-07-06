"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanToolUseValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.json_document
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.uuid


class SpanToolUseValue(TypedDict, closed=True):
    tool_use_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>Unique ID for this tool invocation</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The tool name</p>"""
    arguments: "aws_sdk_qconnect.types.json_document.JSONDocument"
    """<p>The tool input arguments</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanToolUseValue) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    out["arguments"] = value["arguments"]
    return out


def deserialize_json(data: dict) -> SpanToolUseValue:
    out: SpanToolUseValue = {}  # type: ignore[typeddict-item]
    if "toolUseId" in data:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("SpanToolUseValue.tool_use_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SpanToolUseValue.name required")
    if "arguments" in data:
        out["arguments"] = data["arguments"]
    else:
        raise DeserializationError("SpanToolUseValue.arguments required")
    return out
