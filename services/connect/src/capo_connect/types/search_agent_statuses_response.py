"""Generated from Smithy shape ``com.amazonaws.connect#SearchAgentStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_list
    import capo_connect.types.approximate_total_count
    import capo_connect.types.next_token2500


class SearchAgentStatusesResponse(TypedDict, closed=True):
    agent_statuses: NotRequired["capo_connect.types.agent_status_list.AgentStatusList"]
    """<p>The search criteria to be used to return agent statuses.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    approximate_total_count: NotRequired[
        "capo_connect.types.approximate_total_count.ApproximateTotalCount"
    ]
    """<p>The total number of agent statuses which matched your search query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAgentStatusesResponse) -> dict:
    out: dict = {}
    if "agent_statuses" in value:
        import capo_connect.types.agent_status_list

        out["AgentStatuses"] = capo_connect.types.agent_status_list.serialize_json(
            value["agent_statuses"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approximate_total_count" in value:
        out["ApproximateTotalCount"] = value["approximate_total_count"]
    return out


def deserialize_json(data: dict) -> SearchAgentStatusesResponse:
    out: SearchAgentStatusesResponse = {}  # type: ignore[typeddict-item]
    if "AgentStatuses" in data:
        import capo_connect.types.agent_status_list

        out["agent_statuses"] = capo_connect.types.agent_status_list.deserialize_json(
            data["AgentStatuses"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ApproximateTotalCount" in data:
        out["approximate_total_count"] = data["ApproximateTotalCount"]
    return out
