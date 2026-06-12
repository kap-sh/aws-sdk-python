"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteStatementResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.field_list
    import aws_sdk_rds_data.types.formatted_sql_records
    import aws_sdk_rds_data.types.metadata
    import aws_sdk_rds_data.types.records_updated
    import aws_sdk_rds_data.types.sql_records


class ExecuteStatementResponse(TypedDict):
    records: NotRequired["aws_sdk_rds_data.types.sql_records.SqlRecords"]
    """<p>The records returned by the SQL statement. This field is blank if the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p>"""
    column_metadata: NotRequired["aws_sdk_rds_data.types.metadata.Metadata"]
    """<p>Metadata for the columns included in the results. This field is blank if the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p>"""
    number_of_records_updated: "aws_sdk_rds_data.types.records_updated.RecordsUpdated"
    """<p>The number of records updated by the request.</p>"""
    generated_fields: NotRequired["aws_sdk_rds_data.types.field_list.FieldList"]
    """<p>Values for fields generated during a DML request.</p> <note> <p>The <code>generatedFields</code> data isn't supported by Aurora PostgreSQL. To get the values of generated fields, use the <code>RETURNING</code> clause. For more information, see <a href=\"https://www.postgresql.org/docs/10/dml-returning.html\">Returning Data From Modified Rows</a> in the PostgreSQL documentation.</p> </note>"""
    formatted_records: NotRequired[
        "aws_sdk_rds_data.types.formatted_sql_records.FormattedSqlRecords"
    ]
    """<p>A string value that represents the result set of a <code>SELECT</code> statement in JSON format. This value is only present when the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p> <p>The size limit for this field is currently 10 MB. If the JSON-formatted string representing the result set requires more than 10 MB, the call returns an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteStatementResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import aws_sdk_rds_data.types.sql_records

        out["records"] = aws_sdk_rds_data.types.sql_records.serialize_json(
            value["records"]
        )
    if "column_metadata" in value:
        import aws_sdk_rds_data.types.metadata

        out["columnMetadata"] = aws_sdk_rds_data.types.metadata.serialize_json(
            value["column_metadata"]
        )
    out["numberOfRecordsUpdated"] = value.get("number_of_records_updated", 0)
    if "generated_fields" in value:
        import aws_sdk_rds_data.types.field_list

        out["generatedFields"] = aws_sdk_rds_data.types.field_list.serialize_json(
            value["generated_fields"]
        )
    if "formatted_records" in value:
        out["formattedRecords"] = value["formatted_records"]
    return out


def deserialize_json(data: dict) -> ExecuteStatementResponse:
    out: ExecuteStatementResponse = {}  # type: ignore[typeddict-item]
    if "records" in data:
        import aws_sdk_rds_data.types.sql_records

        out["records"] = aws_sdk_rds_data.types.sql_records.deserialize_json(
            data["records"]
        )
    if "columnMetadata" in data:
        import aws_sdk_rds_data.types.metadata

        out["column_metadata"] = aws_sdk_rds_data.types.metadata.deserialize_json(
            data["columnMetadata"]
        )
    if "numberOfRecordsUpdated" in data:
        out["number_of_records_updated"] = data["numberOfRecordsUpdated"]
    else:
        out["number_of_records_updated"] = 0
    if "generatedFields" in data:
        import aws_sdk_rds_data.types.field_list

        out["generated_fields"] = aws_sdk_rds_data.types.field_list.deserialize_json(
            data["generatedFields"]
        )
    if "formattedRecords" in data:
        out["formatted_records"] = data["formattedRecords"]
    return out
