"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorDatabasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.database_list
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorDatabasesResponse(TypedDict, closed=True):
    databases: NotRequired[
        "capo_database_migration_service.types.database_list.DatabaseList"
    ]
    """<p>Provides descriptions of the Fleet Advisor collector databases, including the database's collector, ID, and name.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorDatabasesResponse) -> dict:
    out: dict = {}
    if "databases" in value:
        import capo_database_migration_service.types.database_list

        out["Databases"] = (
            capo_database_migration_service.types.database_list.serialize_aws_json_1_1(
                value["databases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorDatabasesResponse:
    out: DescribeFleetAdvisorDatabasesResponse = {}  # type: ignore[typeddict-item]
    if "Databases" in data:
        import capo_database_migration_service.types.database_list

        out["databases"] = (
            capo_database_migration_service.types.database_list.deserialize_aws_json_1_1(
                data["Databases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
