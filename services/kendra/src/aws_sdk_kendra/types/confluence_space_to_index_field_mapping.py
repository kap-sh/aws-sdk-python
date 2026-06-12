"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceSpaceToIndexFieldMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.confluence_space_field_name
    import aws_sdk_kendra.types.data_source_date_field_format
    import aws_sdk_kendra.types.index_field_name


class ConfluenceSpaceToIndexFieldMapping(TypedDict):
    data_source_field_name: NotRequired[
        "aws_sdk_kendra.types.confluence_space_field_name.ConfluenceSpaceFieldName"
    ]
    """<p>The name of the field in the data source. </p>"""
    date_field_format: NotRequired[
        "aws_sdk_kendra.types.data_source_date_field_format.DataSourceDateFieldFormat"
    ]
    """<p>The format for date fields in the data source. If the field specified in <code>DataSourceFieldName</code> is a date field you must specify the date format. If the field is not a date field, an exception is thrown.</p>"""
    index_field_name: NotRequired[
        "aws_sdk_kendra.types.index_field_name.IndexFieldName"
    ]
    """<p>The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfluenceSpaceToIndexFieldMapping) -> dict:
    out: dict = {}
    if "data_source_field_name" in value:
        import aws_sdk_kendra.types.confluence_space_field_name

        out["DataSourceFieldName"] = (
            aws_sdk_kendra.types.confluence_space_field_name.serialize_aws_json_1_1(
                value["data_source_field_name"]
            )
        )
    if "date_field_format" in value:
        out["DateFieldFormat"] = value["date_field_format"]
    if "index_field_name" in value:
        out["IndexFieldName"] = value["index_field_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfluenceSpaceToIndexFieldMapping:
    out: ConfluenceSpaceToIndexFieldMapping = {}  # type: ignore[typeddict-item]
    if "DataSourceFieldName" in data:
        import aws_sdk_kendra.types.confluence_space_field_name

        out["data_source_field_name"] = (
            aws_sdk_kendra.types.confluence_space_field_name.deserialize_aws_json_1_1(
                data["DataSourceFieldName"]
            )
        )
    if "DateFieldFormat" in data:
        out["date_field_format"] = data["DateFieldFormat"]
    if "IndexFieldName" in data:
        out["index_field_name"] = data["IndexFieldName"]
    return out
