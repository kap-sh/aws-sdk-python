"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_summary_list


class SearchAgentsResponse(TypedDict, closed=True):
    agent_summaries: NotRequired[
        "aws_sdk_quicksight.types.agent_summary_list.AgentSummaryList"
    ]
    """<p>A list of agent summaries.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAgentsResponse) -> dict:
    out: dict = {}
    if "agent_summaries" in value:
        import aws_sdk_quicksight.types.agent_summary_list

        out["AgentSummaries"] = (
            aws_sdk_quicksight.types.agent_summary_list.serialize_json(
                value["agent_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchAgentsResponse:
    out: SearchAgentsResponse = {}  # type: ignore[typeddict-item]
    if "AgentSummaries" in data:
        import aws_sdk_quicksight.types.agent_summary_list

        out["agent_summaries"] = (
            aws_sdk_quicksight.types.agent_summary_list.deserialize_json(
                data["AgentSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
