"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.asset_type
    import aws_sdk_devops_agent.types.next_token


class ListAssetsRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space to list assets from</p>"""
    asset_type: NotRequired["aws_sdk_devops_agent.types.asset_type.AssetType"]
    """<p>Filter results to only assets of this type</p>"""
    updated_after: NotRequired["datetime.datetime"]
    """<p>Filter results to only assets updated after this timestamp</p>"""
    updated_before: NotRequired["datetime.datetime"]
    """<p>Filter results to only assets updated before this timestamp</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token from a previous response to retrieve the next page of results</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single response</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetsRequest:
    out: ListAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
