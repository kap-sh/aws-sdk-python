"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListMigrationTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.max_results
    import capo_migration_hub.types.resource_name
    import capo_migration_hub.types.token


class ListMigrationTasksRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_migration_hub.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""
    max_results: NotRequired["capo_migration_hub.types.max_results.MaxResults"]
    """<p>Value to specify how many results are returned per page.</p>"""
    resource_name: NotRequired["capo_migration_hub.types.resource_name.ResourceName"]
    """<p>Filter migration tasks by discovered resource name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMigrationTasksRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMigrationTasksRequest:
    out: ListMigrationTasksRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    return out
