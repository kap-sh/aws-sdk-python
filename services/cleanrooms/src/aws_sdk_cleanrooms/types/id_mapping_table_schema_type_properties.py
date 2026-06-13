"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingTableSchemaTypeProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.id_mapping_table_input_source_list


class IdMappingTableSchemaTypeProperties(TypedDict):
    id_mapping_table_input_source: "aws_sdk_cleanrooms.types.id_mapping_table_input_source_list.IdMappingTableInputSourceList"
    """<p>Defines which ID namespace associations are used to create the ID mapping table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingTableSchemaTypeProperties) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.id_mapping_table_input_source_list

    out["idMappingTableInputSource"] = (
        aws_sdk_cleanrooms.types.id_mapping_table_input_source_list.serialize_json(
            value["id_mapping_table_input_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> IdMappingTableSchemaTypeProperties:
    out: IdMappingTableSchemaTypeProperties = {}  # type: ignore[typeddict-item]
    if "idMappingTableInputSource" in data:
        import aws_sdk_cleanrooms.types.id_mapping_table_input_source_list

        out["id_mapping_table_input_source"] = (
            aws_sdk_cleanrooms.types.id_mapping_table_input_source_list.deserialize_json(
                data["idMappingTableInputSource"]
            )
        )
    else:
        raise DeserializationError(
            "IdMappingTableSchemaTypeProperties.id_mapping_table_input_source required"
        )
    return out
