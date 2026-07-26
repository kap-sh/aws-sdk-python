"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#OutputFormatStructure``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.json_schema_definition


class _OutputFormatStructure_jsonSchema(TypedDict, closed=True):
    jsonSchema: "capo_bedrock_runtime.types.json_schema_definition.JsonSchemaDefinition"


OutputFormatStructure: TypeAlias = _OutputFormatStructure_jsonSchema


# --- restJson1 ser/de ---
def serialize_json(value: OutputFormatStructure) -> dict:
    if "jsonSchema" in value:
        import capo_bedrock_runtime.types.json_schema_definition

        return {
            "jsonSchema": capo_bedrock_runtime.types.json_schema_definition.serialize_json(
                value["jsonSchema"]
            )
        }
    else:
        raise SerializationError("OutputFormatStructure: no variant present")


def deserialize_json(data: dict) -> OutputFormatStructure:
    if "jsonSchema" in data:
        import capo_bedrock_runtime.types.json_schema_definition

        return {
            "jsonSchema": capo_bedrock_runtime.types.json_schema_definition.deserialize_json(
                data["jsonSchema"]
            )
        }
    else:
        raise DeserializationError("OutputFormatStructure: no recognized variant key")
