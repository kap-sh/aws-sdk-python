"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabasesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_list
    import aws_sdk_lightsail.types.string


class GetRelationalDatabasesResult(TypedDict):
    relational_databases: NotRequired[
        "aws_sdk_lightsail.types.relational_database_list.RelationalDatabaseList"
    ]
    """<p>An object describing the result of your get relational databases request.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetRelationalDatabases</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabasesResult) -> dict:
    out: dict = {}
    if "relational_databases" in value:
        import aws_sdk_lightsail.types.relational_database_list

        out["relationalDatabases"] = (
            aws_sdk_lightsail.types.relational_database_list.serialize_aws_json_1_1(
                value["relational_databases"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabasesResult:
    out: GetRelationalDatabasesResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabases" in data:
        import aws_sdk_lightsail.types.relational_database_list

        out["relational_databases"] = (
            aws_sdk_lightsail.types.relational_database_list.deserialize_aws_json_1_1(
                data["relationalDatabases"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
