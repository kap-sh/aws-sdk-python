"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties


class _SchemaTypeProperties_idMappingTable(TypedDict, closed=True):
    idMappingTable: "aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties.IdMappingTableSchemaTypeProperties"


SchemaTypeProperties: TypeAlias = _SchemaTypeProperties_idMappingTable


# --- restJson1 ser/de ---
def serialize_json(value: SchemaTypeProperties) -> dict:
    if "idMappingTable" in value:
        import aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties

        return {
            "idMappingTable": aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties.serialize_json(
                value["idMappingTable"]
            )
        }
    else:
        raise SerializationError("SchemaTypeProperties: no variant present")


def deserialize_json(data: dict) -> SchemaTypeProperties:
    if "idMappingTable" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties

        return {
            "idMappingTable": aws_sdk_cleanrooms.types.id_mapping_table_schema_type_properties.deserialize_json(
                data["idMappingTable"]
            )
        }
    else:
        raise DeserializationError("SchemaTypeProperties: no recognized variant key")
