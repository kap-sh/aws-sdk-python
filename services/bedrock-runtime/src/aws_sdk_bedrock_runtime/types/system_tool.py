"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SystemTool``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.tool_name


class SystemTool(TypedDict):
    name: "aws_sdk_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the system-defined tool that you want to call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemTool) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SystemTool:
    out: SystemTool = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SystemTool.name required")
    return out
