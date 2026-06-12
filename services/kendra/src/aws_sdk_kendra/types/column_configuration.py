"""Generated from Smithy shape ``com.amazonaws.kendra#ColumnConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.change_detecting_columns
    import aws_sdk_kendra.types.column_name
    import aws_sdk_kendra.types.data_source_to_index_field_mapping_list


class ColumnConfiguration(TypedDict):
    document_id_column_name: "aws_sdk_kendra.types.column_name.ColumnName"
    """<p>The column that provides the document's identifier.</p>"""
    document_data_column_name: "aws_sdk_kendra.types.column_name.ColumnName"
    """<p>The column that contains the contents of the document.</p>"""
    document_title_column_name: NotRequired[
        "aws_sdk_kendra.types.column_name.ColumnName"
    ]
    """<p>The column that contains the title of the document.</p>"""
    field_mappings: NotRequired[
        "aws_sdk_kendra.types.data_source_to_index_field_mapping_list.DataSourceToIndexFieldMappingList"
    ]
    """<p>An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the <code>UpdateIndex</code> API.</p>"""
    change_detecting_columns: (
        "aws_sdk_kendra.types.change_detecting_columns.ChangeDetectingColumns"
    )
    """<p>One to five columns that indicate when a document in the database has changed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnConfiguration) -> dict:
    out: dict = {}
    out["DocumentIdColumnName"] = value["document_id_column_name"]
    out["DocumentDataColumnName"] = value["document_data_column_name"]
    if "document_title_column_name" in value:
        out["DocumentTitleColumnName"] = value["document_title_column_name"]
    if "field_mappings" in value:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["FieldMappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.serialize_aws_json_1_1(
                value["field_mappings"]
            )
        )
    import aws_sdk_kendra.types.change_detecting_columns

    out["ChangeDetectingColumns"] = (
        aws_sdk_kendra.types.change_detecting_columns.serialize_aws_json_1_1(
            value["change_detecting_columns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnConfiguration:
    out: ColumnConfiguration = {}  # type: ignore[typeddict-item]
    if "DocumentIdColumnName" in data:
        out["document_id_column_name"] = data["DocumentIdColumnName"]
    else:
        raise DeserializationError(
            "ColumnConfiguration.document_id_column_name required"
        )
    if "DocumentDataColumnName" in data:
        out["document_data_column_name"] = data["DocumentDataColumnName"]
    else:
        raise DeserializationError(
            "ColumnConfiguration.document_data_column_name required"
        )
    if "DocumentTitleColumnName" in data:
        out["document_title_column_name"] = data["DocumentTitleColumnName"]
    if "FieldMappings" in data:
        import aws_sdk_kendra.types.data_source_to_index_field_mapping_list

        out["field_mappings"] = (
            aws_sdk_kendra.types.data_source_to_index_field_mapping_list.deserialize_aws_json_1_1(
                data["FieldMappings"]
            )
        )
    if "ChangeDetectingColumns" in data:
        import aws_sdk_kendra.types.change_detecting_columns

        out["change_detecting_columns"] = (
            aws_sdk_kendra.types.change_detecting_columns.deserialize_aws_json_1_1(
                data["ChangeDetectingColumns"]
            )
        )
    else:
        raise DeserializationError(
            "ColumnConfiguration.change_detecting_columns required"
        )
    return out
