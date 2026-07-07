"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RecordColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.record_column_mapping
    import aws_sdk_kinesis_analytics_v2.types.record_column_name
    import aws_sdk_kinesis_analytics_v2.types.record_column_sql_type


class RecordColumn(TypedDict, closed=True):
    name: "aws_sdk_kinesis_analytics_v2.types.record_column_name.RecordColumnName"
    """<p>The name of the column that is created in the in-application input stream or reference table.</p>"""
    mapping: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.record_column_mapping.RecordColumnMapping"
    ]
    """<p>A reference to the data element in the streaming input or the reference data source.</p>"""
    sql_type: (
        "aws_sdk_kinesis_analytics_v2.types.record_column_sql_type.RecordColumnSqlType"
    )
    """<p>The type of column created in the in-application input stream or reference table.</p>"""


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
