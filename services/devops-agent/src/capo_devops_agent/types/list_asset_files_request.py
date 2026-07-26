"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetFilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.resource_id


class ListAssetFilesRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset whose files to list</p>"""
    asset_version: NotRequired["int"]
    """<p>The specific asset version to list files from. If omitted, files from the latest version are returned.</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token from a previous response to retrieve the next page of results</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single response</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetFilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetFilesRequest:
    out: ListAssetFilesRequest = {}  # type: ignore[typeddict-item]
    return out
