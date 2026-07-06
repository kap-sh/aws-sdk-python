"""Generated from Smithy shape ``com.amazonaws.quicksight#ImportTableOperationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_column_id_mapping_list
    import aws_sdk_quicksight.types.data_set_entity_resource_id


class ImportTableOperationSource(TypedDict, closed=True):
    source_table_id: (
        "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the source table to import data from.</p>"""
    column_id_mappings: NotRequired[
        "aws_sdk_quicksight.types.data_set_column_id_mapping_list.DataSetColumnIdMappingList"
    ]
    """<p>The mappings between source column identifiers and target column identifiers during the import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTableOperationSource) -> dict:
    out: dict = {}
    out["SourceTableId"] = value["source_table_id"]
    if "column_id_mappings" in value:
        import aws_sdk_quicksight.types.data_set_column_id_mapping_list

        out["ColumnIdMappings"] = (
            aws_sdk_quicksight.types.data_set_column_id_mapping_list.serialize_json(
                value["column_id_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportTableOperationSource:
    out: ImportTableOperationSource = {}  # type: ignore[typeddict-item]
    if "SourceTableId" in data:
        out["source_table_id"] = data["SourceTableId"]
    else:
        raise DeserializationError(
            "ImportTableOperationSource.source_table_id required"
        )
    if "ColumnIdMappings" in data:
        import aws_sdk_quicksight.types.data_set_column_id_mapping_list

        out["column_id_mappings"] = (
            aws_sdk_quicksight.types.data_set_column_id_mapping_list.deserialize_json(
                data["ColumnIdMappings"]
            )
        )
    return out
