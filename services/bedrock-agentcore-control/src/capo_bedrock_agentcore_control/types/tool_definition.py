"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ToolDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.schema_definition


class ToolDefinition(TypedDict, closed=True):
    name: "str"
    """<p>The name of the tool. This name identifies the tool in the Model Context Protocol.</p>"""
    description: "str"
    """<p>The description of the tool. This description provides information about the purpose and usage of the tool.</p>"""
    input_schema: (
        "capo_bedrock_agentcore_control.types.schema_definition.SchemaDefinition"
    )
    """<p>The input schema for the tool. This schema defines the structure of the input that the tool accepts.</p>"""
    output_schema: NotRequired[
        "capo_bedrock_agentcore_control.types.schema_definition.SchemaDefinition"
    ]
    """<p>The output schema for the tool. This schema defines the structure of the output that the tool produces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.schema_definition

    out["inputSchema"] = (
        capo_bedrock_agentcore_control.types.schema_definition.serialize_json(
            value["input_schema"]
        )
    )
    if "output_schema" in value:
        import capo_bedrock_agentcore_control.types.schema_definition

        out["outputSchema"] = (
            capo_bedrock_agentcore_control.types.schema_definition.serialize_json(
                value["output_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> ToolDefinition:
    out: ToolDefinition = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ToolDefinition.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("ToolDefinition.description required")
    if "inputSchema" in data:
        import capo_bedrock_agentcore_control.types.schema_definition

        out["input_schema"] = (
            capo_bedrock_agentcore_control.types.schema_definition.deserialize_json(
                data["inputSchema"]
            )
        )
    else:
        raise DeserializationError("ToolDefinition.input_schema required")
    if "outputSchema" in data:
        import capo_bedrock_agentcore_control.types.schema_definition

        out["output_schema"] = (
            capo_bedrock_agentcore_control.types.schema_definition.deserialize_json(
                data["outputSchema"]
            )
        )
    return out
