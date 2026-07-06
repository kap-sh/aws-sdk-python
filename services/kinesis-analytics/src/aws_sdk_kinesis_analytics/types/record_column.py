"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#RecordColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.record_column_mapping
    import aws_sdk_kinesis_analytics.types.record_column_name
    import aws_sdk_kinesis_analytics.types.record_column_sql_type


class RecordColumn(TypedDict, closed=True):
    name: "aws_sdk_kinesis_analytics.types.record_column_name.RecordColumnName"
    """<p>Name of the column created in the in-application input stream or reference table.</p>"""
    mapping: NotRequired[
        "aws_sdk_kinesis_analytics.types.record_column_mapping.RecordColumnMapping"
    ]
    r"""<p>Reference to the data element in the streaming input or the reference data source. This element is required if the <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel\">RecordFormatType</a> is <code>JSON</code>.</p>"""
    sql_type: (
        "aws_sdk_kinesis_analytics.types.record_column_sql_type.RecordColumnSqlType"
    )
    """<p>Type of column created in the in-application input stream or reference table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "mapping" in value:
        out["Mapping"] = value["mapping"]
    out["SqlType"] = value["sql_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordColumn:
    out: RecordColumn = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RecordColumn.name required")
    if "Mapping" in data:
        out["mapping"] = data["Mapping"]
    if "SqlType" in data:
        out["sql_type"] = data["SqlType"]
    else:
        raise DeserializationError("RecordColumn.sql_type required")
    return out
