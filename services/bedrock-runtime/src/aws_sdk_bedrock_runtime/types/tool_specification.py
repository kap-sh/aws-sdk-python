"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_empty_string
    import aws_sdk_bedrock_runtime.types.tool_input_schema
    import aws_sdk_bedrock_runtime.types.tool_name


class ToolSpecification(TypedDict):
    name: "aws_sdk_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name for the tool.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description for the tool.</p>"""
    input_schema: "aws_sdk_bedrock_runtime.types.tool_input_schema.ToolInputSchema"
    """<p>The input schema for the tool in JSON format.</p>"""
    strict: NotRequired["bool"]
    """<p>Flag to enable structured output enforcement on a tool usage response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpecification) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_runtime.types.tool_input_schema

    out["inputSchema"] = aws_sdk_bedrock_runtime.types.tool_input_schema.serialize_json(
        value["input_schema"]
    )
    if "strict" in value:
        out["strict"] = value["strict"]
    return out


def deserialize_json(data: dict) -> ToolSpecification:
    out: ToolSpecification = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ToolSpecification.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "inputSchema" in data:
        import aws_sdk_bedrock_runtime.types.tool_input_schema

        out["input_schema"] = (
            aws_sdk_bedrock_runtime.types.tool_input_schema.deserialize_json(
                data["inputSchema"]
            )
        )
    else:
        raise DeserializationError("ToolSpecification.input_schema required")
    if "strict" in data:
        out["strict"] = data["strict"]
    return out
