"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListDiscoveredResourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.max_results_resources
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.progress_update_stream
    import aws_sdk_migration_hub.types.token


class ListDiscoveredResourcesRequest(TypedDict):
    progress_update_stream: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream.</p>"""
    migration_task_name: (
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The name of the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If a <code>NextToken</code> was returned by a previous call, there are more results available. To retrieve the next page of results, make the call again using the returned token in <code>NextToken</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_migration_hub.types.max_results_resources.MaxResultsResources"
    ]
    """<p>The maximum number of results returned per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDiscoveredResourcesRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDiscoveredResourcesRequest:
    out: ListDiscoveredResourcesRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "ListDiscoveredResourcesRequest.progress_update_stream required"
        )
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "ListDiscoveredResourcesRequest.migration_task_name required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
