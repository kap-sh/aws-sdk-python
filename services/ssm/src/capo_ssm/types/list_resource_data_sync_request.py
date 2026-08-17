"""Generated from Smithy shape ``com.amazonaws.ssm#ListResourceDataSyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.resource_data_sync_type


class ListResourceDataSyncRequest(TypedDict, closed=True):
    sync_type: NotRequired[
        "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    """<p>View a list of resource data syncs according to the sync type. Specify <code>SyncToDestination</code> to view resource data syncs that synchronize data to an Amazon S3 bucket. Specify <code>SyncFromSource</code> to view resource data syncs from Organizations or from multiple Amazon Web Services Regions.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceDataSyncRequest) -> dict:
    out: dict = {}
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceDataSyncRequest:
    out: ListResourceDataSyncRequest = {}  # type: ignore[typeddict-item]
    if data.get("SyncType") is not None:
        out["sync_type"] = data["SyncType"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
