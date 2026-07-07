"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListDatabasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.database_list
    import aws_sdk_redshift_data.types.string


class ListDatabasesResponse(TypedDict, closed=True):
    databases: NotRequired["aws_sdk_redshift_data.types.database_list.DatabaseList"]
    """<p>The names of databases. </p>"""
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatabasesResponse) -> dict:
    out: dict = {}
    if "databases" in value:
        import aws_sdk_redshift_data.types.database_list

        out["Databases"] = (
            aws_sdk_redshift_data.types.database_list.serialize_aws_json_1_1(
                value["databases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatabasesResponse:
    out: ListDatabasesResponse = {}  # type: ignore[typeddict-item]
    if "Databases" in data:
        import aws_sdk_redshift_data.types.database_list

        out["databases"] = (
            aws_sdk_redshift_data.types.database_list.deserialize_aws_json_1_1(
                data["Databases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
