"""Generated from Smithy shape ``com.amazonaws.novaact#ToolSpec``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.tool_description
    import aws_sdk_nova_act.types.tool_input_schema
    import aws_sdk_nova_act.types.tool_name


class ToolSpec(TypedDict):
    name: "aws_sdk_nova_act.types.tool_name.ToolName"
    """<p>The unique name of the tool that acts will use to invoke it.</p>"""
    description: "aws_sdk_nova_act.types.tool_description.ToolDescription"
    """<p>A description of what the tool does and how it should be used.</p>"""
    input_schema: "aws_sdk_nova_act.types.tool_input_schema.ToolInputSchema"
    """<p>The JSON schema that defines the expected input format for the tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpec) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    import aws_sdk_nova_act.types.tool_input_schema

    out["inputSchema"] = aws_sdk_nova_act.types.tool_input_schema.serialize_json(
        value["input_schema"]
    )
    return out


def deserialize_json(data: dict) -> ToolSpec:
    out: ToolSpec = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ToolSpec.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("ToolSpec.description required")
    if "inputSchema" in data:
        import aws_sdk_nova_act.types.tool_input_schema

        out["input_schema"] = aws_sdk_nova_act.types.tool_input_schema.deserialize_json(
            data["inputSchema"]
        )
    else:
        raise DeserializationError("ToolSpec.input_schema required")
    return out
