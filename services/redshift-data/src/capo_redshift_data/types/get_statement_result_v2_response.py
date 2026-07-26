"""Generated from Smithy shape ``com.amazonaws.redshiftdata#GetStatementResultV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_data.types.column_metadata_list
    import capo_redshift_data.types.formatted_sql_records
    import capo_redshift_data.types.long
    import capo_redshift_data.types.result_format_string
    import capo_redshift_data.types.string


class GetStatementResultV2Response(TypedDict, closed=True):
    records: "capo_redshift_data.types.formatted_sql_records.FormattedSqlRecords"
    """<p>The results of the SQL statement in CSV format.</p>"""
    column_metadata: NotRequired[
        "capo_redshift_data.types.column_metadata_list.ColumnMetadataList"
    ]
    """<p>The properties (metadata) of a column.</p>"""
    total_num_rows: "capo_redshift_data.types.long.Long"
    """<p>The total number of rows in the result set returned from a query. You can use this number to estimate the number of calls to the <code>GetStatementResultV2</code> operation needed to page through the results. </p>"""
    result_format: NotRequired[
        "capo_redshift_data.types.result_format_string.ResultFormatString"
    ]
    """<p>The data format of the result of the SQL statement.</p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStatementResultV2Response) -> dict:
    out: dict = {}
    import capo_redshift_data.types.formatted_sql_records

    out["Records"] = (
        capo_redshift_data.types.formatted_sql_records.serialize_aws_json_1_1(
            value["records"]
        )
    )
    if "column_metadata" in value:
        import capo_redshift_data.types.column_metadata_list

        out["ColumnMetadata"] = (
            capo_redshift_data.types.column_metadata_list.serialize_aws_json_1_1(
                value["column_metadata"]
            )
        )
    out["TotalNumRows"] = value.get("total_num_rows", 0)
    if "result_format" in value:
        out["ResultFormat"] = value["result_format"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStatementResultV2Response:
    out: GetStatementResultV2Response = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import capo_redshift_data.types.formatted_sql_records

        out["records"] = (
            capo_redshift_data.types.formatted_sql_records.deserialize_aws_json_1_1(
                data["Records"]
            )
        )
    else:
        raise DeserializationError("GetStatementResultV2Response.records required")
    if "ColumnMetadata" in data:
        import capo_redshift_data.types.column_metadata_list

        out["column_metadata"] = (
            capo_redshift_data.types.column_metadata_list.deserialize_aws_json_1_1(
                data["ColumnMetadata"]
            )
        )
    if "TotalNumRows" in data:
        out["total_num_rows"] = data["TotalNumRows"]
    else:
        out["total_num_rows"] = 0
    if "ResultFormat" in data:
        out["result_format"] = data["ResultFormat"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
