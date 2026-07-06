"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.resource_id


class ListAssetVersionsRequest(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the asset</p>"""
    asset_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the asset whose versions to list</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single response</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token from a previous response to retrieve the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetVersionsRequest:
    out: ListAssetVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
