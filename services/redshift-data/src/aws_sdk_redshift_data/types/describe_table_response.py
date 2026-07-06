"""Generated from Smithy shape ``com.amazonaws.redshiftdata#DescribeTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.column_list
    import aws_sdk_redshift_data.types.string


class DescribeTableResponse(TypedDict, closed=True):
    table_name: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>The table name. </p>"""
    column_list: NotRequired["aws_sdk_redshift_data.types.column_list.ColumnList"]
    """<p>A list of columns in the table. </p>"""
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTableResponse) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "column_list" in value:
        import aws_sdk_redshift_data.types.column_list

        out["ColumnList"] = (
            aws_sdk_redshift_data.types.column_list.serialize_aws_json_1_1(
                value["column_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTableResponse:
    out: DescribeTableResponse = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "ColumnList" in data:
        import aws_sdk_redshift_data.types.column_list

        out["column_list"] = (
            aws_sdk_redshift_data.types.column_list.deserialize_aws_json_1_1(
                data["ColumnList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
