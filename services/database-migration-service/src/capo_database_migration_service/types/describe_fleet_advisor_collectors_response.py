"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorCollectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.collector_responses
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorCollectorsResponse(TypedDict, closed=True):
    collectors: NotRequired[
        "capo_database_migration_service.types.collector_responses.CollectorResponses"
    ]
    """<p>Provides descriptions of the Fleet Advisor collectors, including the collectors' name and ID, and the latest inventory data. </p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorCollectorsResponse) -> dict:
    out: dict = {}
    if "collectors" in value:
        import capo_database_migration_service.types.collector_responses

        out["Collectors"] = (
            capo_database_migration_service.types.collector_responses.serialize_aws_json_1_1(
                value["collectors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorCollectorsResponse:
    out: DescribeFleetAdvisorCollectorsResponse = {}  # type: ignore[typeddict-item]
    if "Collectors" in data:
        import capo_database_migration_service.types.collector_responses

        out["collectors"] = (
            capo_database_migration_service.types.collector_responses.deserialize_aws_json_1_1(
                data["Collectors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
