"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListSyncResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.sync_resource_filters
    import capo_iottwinmaker.types.sync_source


class ListSyncResourcesRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the sync job.</p>"""
    sync_source: "capo_iottwinmaker.types.sync_source.SyncSource"
    """<p>The sync source.</p> <note> <p>Currently the only supported syncSource is <code>SITEWISE </code>.</p> </note>"""
    filters: NotRequired[
        "capo_iottwinmaker.types.sync_resource_filters.SyncResourceFilters"
    ]
    """<p>A list of objects that filter the request.</p> <p>The following filter combinations are supported:</p> <ul> <li> <p>Filter with state</p> </li> <li> <p>Filter with ResourceType and ResourceId</p> </li> <li> <p>Filter with ResourceType and ExternalId</p> </li> </ul>"""
    max_results: NotRequired["capo_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 50.</p> <p>Valid Range: Minimum value of 0. Maximum value of 200.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSyncResourcesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_iottwinmaker.types.sync_resource_filters

        out["filters"] = capo_iottwinmaker.types.sync_resource_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSyncResourcesRequest:
    out: ListSyncResourcesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_iottwinmaker.types.sync_resource_filters

        out["filters"] = capo_iottwinmaker.types.sync_resource_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
