"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.string
    import aws_sdk_redshift_data.types.table_list


class ListTablesResponse(TypedDict):
    tables: NotRequired["aws_sdk_redshift_data.types.table_list.TableList"]
    """<p>The tables that match the request pattern. </p>"""
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTablesResponse) -> dict:
    out: dict = {}
    if "tables" in value:
        import aws_sdk_redshift_data.types.table_list

        out["Tables"] = aws_sdk_redshift_data.types.table_list.serialize_aws_json_1_1(
            value["tables"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTablesResponse:
    out: ListTablesResponse = {}  # type: ignore[typeddict-item]
    if "Tables" in data:
        import aws_sdk_redshift_data.types.table_list

        out["tables"] = aws_sdk_redshift_data.types.table_list.deserialize_aws_json_1_1(
            data["Tables"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
