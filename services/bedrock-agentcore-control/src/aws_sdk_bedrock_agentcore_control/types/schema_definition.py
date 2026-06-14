"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SchemaDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.required_properties
    import aws_sdk_bedrock_agentcore_control.types.schema_definition
    import aws_sdk_bedrock_agentcore_control.types.schema_properties
    import aws_sdk_bedrock_agentcore_control.types.schema_type


class SchemaDefinition(TypedDict):
    type: "aws_sdk_bedrock_agentcore_control.types.schema_type.SchemaType"
    """<p>The type of the schema definition. This field specifies the data type of the schema.</p>"""
    properties: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_properties.SchemaProperties"
    ]
    """<p>The properties of the schema definition. These properties define the fields in the schema.</p>"""
    required: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.required_properties.RequiredProperties"
    ]
    """<p>The required fields in the schema definition. These fields must be provided when using the schema.</p>"""
    items: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.schema_definition.SchemaDefinition"
    ]
    """<p>The items in the schema definition. This field is used for array types to define the structure of the array elements.</p>"""
    description: NotRequired["str"]
    """<p>The description of the schema definition. This description provides information about the purpose and usage of the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaDefinition) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.schema_type

    out["type"] = aws_sdk_bedrock_agentcore_control.types.schema_type.serialize_json(
        value["type"]
    )
    if "properties" in value:
        import aws_sdk_bedrock_agentcore_control.types.schema_properties

        out["properties"] = (
            aws_sdk_bedrock_agentcore_control.types.schema_properties.serialize_json(
                value["properties"]
            )
        )
    if "required" in value:
        import aws_sdk_bedrock_agentcore_control.types.required_properties

        out["required"] = (
            aws_sdk_bedrock_agentcore_control.types.required_properties.serialize_json(
                value["required"]
            )
        )
    if "items" in value:
        import aws_sdk_bedrock_agentcore_control.types.schema_definition

        out["items"] = (
            aws_sdk_bedrock_agentcore_control.types.schema_definition.serialize_json(
                value["items"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> SchemaDefinition:
    out: SchemaDefinition = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.schema_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.schema_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("SchemaDefinition.type required")
    if "properties" in data:
        import aws_sdk_bedrock_agentcore_control.types.schema_properties

        out["properties"] = (
            aws_sdk_bedrock_agentcore_control.types.schema_properties.deserialize_json(
                data["properties"]
            )
        )
    if "required" in data:
        import aws_sdk_bedrock_agentcore_control.types.required_properties

        out["required"] = (
            aws_sdk_bedrock_agentcore_control.types.required_properties.deserialize_json(
                data["required"]
            )
        )
    if "items" in data:
        import aws_sdk_bedrock_agentcore_control.types.schema_definition

        out["items"] = (
            aws_sdk_bedrock_agentcore_control.types.schema_definition.deserialize_json(
                data["items"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
