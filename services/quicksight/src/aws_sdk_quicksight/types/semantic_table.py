"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticTable``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_entity_resource_id
    import aws_sdk_quicksight.types.row_level_permission_configuration
    import aws_sdk_quicksight.types.semantic_table_alias
    import aws_sdk_quicksight.types.table_semantic_metadata


class SemanticTable(TypedDict):
    alias: "aws_sdk_quicksight.types.semantic_table_alias.SemanticTableAlias"
    """<p>Alias for the semantic table.</p>"""
    destination_table_id: (
        "aws_sdk_quicksight.types.data_set_entity_resource_id.DataSetEntityResourceId"
    )
    """<p>The identifier of the destination table from data preparation that provides data to this semantic table.</p>"""
    row_level_permission_configuration: NotRequired[
        "aws_sdk_quicksight.types.row_level_permission_configuration.RowLevelPermissionConfiguration"
    ]
    """<p>Configuration for row level security that control data access for this semantic table.</p>"""
    semantic_metadata: NotRequired[
        "aws_sdk_quicksight.types.table_semantic_metadata.TableSemanticMetadata"
    ]
    """<p>The column-level semantic metadata for this semantic table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticTable) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    out["DestinationTableId"] = value["destination_table_id"]
    if "row_level_permission_configuration" in value:
        import aws_sdk_quicksight.types.row_level_permission_configuration

        out["RowLevelPermissionConfiguration"] = (
            aws_sdk_quicksight.types.row_level_permission_configuration.serialize_json(
                value["row_level_permission_configuration"]
            )
        )
    if "semantic_metadata" in value:
        import aws_sdk_quicksight.types.table_semantic_metadata

        out["SemanticMetadata"] = (
            aws_sdk_quicksight.types.table_semantic_metadata.serialize_json(
                value["semantic_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticTable:
    out: SemanticTable = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("SemanticTable.alias required")
    if "DestinationTableId" in data:
        out["destination_table_id"] = data["DestinationTableId"]
    else:
        raise DeserializationError("SemanticTable.destination_table_id required")
    if "RowLevelPermissionConfiguration" in data:
        import aws_sdk_quicksight.types.row_level_permission_configuration

        out["row_level_permission_configuration"] = (
            aws_sdk_quicksight.types.row_level_permission_configuration.deserialize_json(
                data["RowLevelPermissionConfiguration"]
            )
        )
    if "SemanticMetadata" in data:
        import aws_sdk_quicksight.types.table_semantic_metadata

        out["semantic_metadata"] = (
            aws_sdk_quicksight.types.table_semantic_metadata.deserialize_json(
                data["SemanticMetadata"]
            )
        )
    return out
