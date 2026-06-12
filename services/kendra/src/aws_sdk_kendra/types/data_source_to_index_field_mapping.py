"""Generated from Smithy shape ``com.amazonaws.kendra#DataSourceToIndexFieldMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_date_field_format
    import aws_sdk_kendra.types.data_source_field_name
    import aws_sdk_kendra.types.index_field_name


class DataSourceToIndexFieldMapping(TypedDict):
    data_source_field_name: (
        "aws_sdk_kendra.types.data_source_field_name.DataSourceFieldName"
    )
    """<p>The name of the field in the data source. You must first create the index field using the <code>UpdateIndex</code> API.</p>"""
    date_field_format: NotRequired[
        "aws_sdk_kendra.types.data_source_date_field_format.DataSourceDateFieldFormat"
    ]
    """<p>The format for date fields in the data source. If the field specified in <code>DataSourceFieldName</code> is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.</p>"""
    index_field_name: "aws_sdk_kendra.types.index_field_name.IndexFieldName"
    """<p>The name of the index field to map to the data source field. The index field type must match the data source field type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceToIndexFieldMapping) -> dict:
    out: dict = {}
    out["DataSourceFieldName"] = value["data_source_field_name"]
    if "date_field_format" in value:
        out["DateFieldFormat"] = value["date_field_format"]
    out["IndexFieldName"] = value["index_field_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceToIndexFieldMapping:
    out: DataSourceToIndexFieldMapping = {}  # type: ignore[typeddict-item]
    if "DataSourceFieldName" in data:
        out["data_source_field_name"] = data["DataSourceFieldName"]
    else:
        raise DeserializationError(
            "DataSourceToIndexFieldMapping.data_source_field_name required"
        )
    if "DateFieldFormat" in data:
        out["date_field_format"] = data["DateFieldFormat"]
    if "IndexFieldName" in data:
        out["index_field_name"] = data["IndexFieldName"]
    else:
        raise DeserializationError(
            "DataSourceToIndexFieldMapping.index_field_name required"
        )
    return out
