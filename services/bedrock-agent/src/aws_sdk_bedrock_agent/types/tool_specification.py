"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ToolSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.non_empty_string
    import aws_sdk_bedrock_agent.types.tool_input_schema
    import aws_sdk_bedrock_agent.types.tool_name


class ToolSpecification(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent.types.tool_name.ToolName"
    """<p>The name of the tool.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the tool.</p>"""
    input_schema: "aws_sdk_bedrock_agent.types.tool_input_schema.ToolInputSchema"
    """<p>The input schema for the tool.</p>"""
    strict: NotRequired["bool"]
    """Whether to enforce strict JSON schema adherence for the tool input"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpecification) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.tool_input_schema

    out["inputSchema"] = aws_sdk_bedrock_agent.types.tool_input_schema.serialize_json(
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
        import aws_sdk_bedrock_agent.types.tool_input_schema

        out["input_schema"] = (
            aws_sdk_bedrock_agent.types.tool_input_schema.deserialize_json(
                data["inputSchema"]
            )
        )
    else:
        raise DeserializationError("ToolSpecification.input_schema required")
    if "strict" in data:
        out["strict"] = data["strict"]
    return out
